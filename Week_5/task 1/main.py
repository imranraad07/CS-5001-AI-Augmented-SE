# main.py
import argparse
from core.github_tools import GitHubTools
from core.state import AgentState
from core.agents import Reviewer, Planner, Writer, Gatekeeper

def run_review_flow(base_branch):
    tools = GitHubTools()
    state = AgentState(diff=tools.get_diff(base=base_branch))
    
    # 1. Review
    state.review_summary = Reviewer().analyze(state.diff)
    
    # 2. Planning
    state.plan = Planner().decide(state.review_summary)
    
    # 3. Writing
    state.draft_content = Writer().draft(state.plan, state.diff)
    
    # 4. Reflection (Critic)
    state.reflection_verdict = Gatekeeper().reflect(state.draft_content, state.diff)
    print(f"[Gatekeeper] Reflection verdict: {state.reflection_verdict}")
    
    if "FAIL" in state.reflection_verdict:
        print("Aborting: Draft failed reflection.")
        return

    # 5. Human Approval
    print(f"\n--- PROPOSED DRAFT ---\n{state.draft_content['title']}\n{state.draft_content['body']}\n")
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