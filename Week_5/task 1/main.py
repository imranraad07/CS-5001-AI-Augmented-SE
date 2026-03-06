# main.py
import argparse
from core.github_tools import GitHubTools
from core.state import AgentState
from core.agents import Reviewer, Planner, Writer, Gatekeeper

def run_review_flow(base_branch):
    tools = GitHubTools()
    state = AgentState(diff=tools.get_diff(base=base_branch))

    # 1. Review — returns structured dict with category, risk, files, issues
    review = Reviewer().analyze(state.diff)
    state.category        = review["category"]
    state.risk_level      = review["risk"]
    state.review_summary  = review["summary"]

    # 2. Planning — evidence-backed decision
    plan = Planner().decide(review)
    state.plan = plan["action"]

    if plan["action"] == "no_action":
        print("\n[Planner] No action required — diff is empty or trivial.")
        return

    # 3. Writing — full draft with evidence, risk, test plan
    state.draft_content = Writer().draft(plan, state.diff)

    # 4. Reflection (Gatekeeper)
    state.reflection_verdict = Gatekeeper().reflect(state.draft_content, state.diff)
    print(f"[Gatekeeper] Reflection verdict: {state.reflection_verdict}")

    if "FAIL" in state.reflection_verdict:
        print("Aborting: Draft failed reflection.")
        return

    # 5. Human Approval
    print(f"\n{'='*60}")
    print(f"  Category  : {state.category}")
    print(f"  Risk      : {state.risk_level}")
    print(f"  Action    : {state.plan}")
    print(f"{'='*60}")
    print(f"\n--- PROPOSED DRAFT ---\n{state.draft_content['title']}\n")
    print(state.draft_content['body'])
    confirm = input("Approve and create? (y/n): ")

    if confirm.lower() == 'y':
        tools.create_on_github(state.draft_content['title'], state.draft_content['body'])
    else:
        print("[Gatekeeper] Draft rejected. Safe abort.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="GitHub Agent")
    parser.add_argument("command", choices=["review", "draft", "improve"])
    parser.add_argument("--base", default="main")
    args = parser.parse_args()

    if args.command == "review":
        run_review_flow(args.base)