# main.py
import argparse
from core.github_tools import GitHubTools
from core.state import AgentState
from core.agents import Reviewer, Planner, Writer, Gatekeeper, InstructionDrafter


# ── review command ────────────────────────────────────────────────────────────

def run_review_flow(base_branch):
    tools = GitHubTools()
    state = AgentState(diff=tools.get_diff(base=base_branch))

    # 1. Review — returns structured dict with category, risk, files, issues
    review = Reviewer().analyze(state.diff)
    state.category       = review["category"]
    state.risk_level     = review["risk"]
    state.review_summary = review["summary"]

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

    _human_approval(state, tools)


# ── draft command ─────────────────────────────────────────────────────────────

def run_draft_flow(draft_type: str, instruction: str):
    """
    Create a GitHub Issue or PR draft from a plain-language instruction.
    No git diff is required — the agent reasons from the instruction alone.
    """
    state = AgentState()   # no diff needed

    # 1. Instruction-based drafting
    drafter = InstructionDrafter()
    state.draft_content = drafter.draft(instruction, draft_type)
    state.category   = draft_type                          # "issue" or "pr"
    state.risk_level = drafter._last_risk                  # captured below
    state.plan       = state.draft_content["action"]

    # 2. Reflection — diff is empty string; Gatekeeper checks structural quality
    state.reflection_verdict = Gatekeeper().reflect(state.draft_content, diff="")
    print(f"[Gatekeeper] Reflection verdict: {state.reflection_verdict}")

    if "FAIL" in state.reflection_verdict:
        print("Aborting: Draft failed reflection.")
        return

    tools = GitHubTools()
    _human_approval(state, tools)


# ── shared approval step ──────────────────────────────────────────────────────

def _human_approval(state: AgentState, tools: GitHubTools):
    print(f"\n{'='*60}")
    print(f"  Category  : {state.category}")
    print(f"  Risk      : {state.risk_level}")
    print(f"  Action    : {state.plan}")
    print(f"{'='*60}")
    print(f"\n--- PROPOSED DRAFT ---\n{state.draft_content['title']}\n")
    print(state.draft_content['body'])

    confirm = input("Approve and create? (y/n): ")
    if confirm.lower() == 'y':
        is_pr = (state.plan == "create_pr")
        tools.create_on_github(state.draft_content['title'],
                               state.draft_content['body'],
                               is_pr=is_pr)
    else:
        print("[Gatekeeper] Draft rejected. Safe abort.")


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="GitHub Agent — AI-powered issue & PR assistant",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # review sub-command
    review_p = subparsers.add_parser(
        "review",
        help="Analyze a git diff and create an issue/PR automatically."
    )
    review_p.add_argument(
        "--base", default="main",
        help="Base branch/ref for the diff (default: main). Use HEAD~1 for latest commit."
    )

    # draft sub-command
    draft_p = subparsers.add_parser(
        "draft",
        help="Create an issue or PR draft from a plain-language instruction."
    )
    draft_p.add_argument(
        "type", choices=["issue", "pr"],
        help="What to create."
    )
    draft_p.add_argument(
        "--instruction", required=True,
        help='Natural-language description, e.g. "Add rate limiting to login endpoint"'
    )

    args = parser.parse_args()

    if args.command == "review":
        run_review_flow(args.base)
    elif args.command == "draft":
        run_draft_flow(args.type, args.instruction)