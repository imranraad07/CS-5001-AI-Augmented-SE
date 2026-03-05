# core/agents.py
class Reviewer:
    def analyze(self, diff):
        print("[Reviewer] Analyzing code changes...")
        # Prompt logic: Categorize (bug/feat), assess risk, find issues.
        return "Review: Detected missing error handling in gateway.py. Risk: Medium."

class Planner:
    def decide(self, review):
        print("[Planner] Deciding next steps...")
        # Planning Pattern: Decide if we need an Issue, PR, or nothing.
        return "Action: Create Issue for error handling improvement."

class Writer:
    def draft(self, action_plan, diff):
        print("[Writer] Drafting content...")
        # Drafts the Title, Body, Evidence, and Test Plan.
        return {
            "title": "Enhance Error Handling in Gateway",
            "body": f"Problem: Gateway fails silently.\nEvidence: {diff[:100]}...\nCriteria: Add try-except."
        }

class Gatekeeper:
    def reflect(self, draft, diff):
        print("[Gatekeeper] Reflection Pattern: Checking for hallucinations...")
        # Reflection Pattern: Is the evidence in the draft actually in the diff?
        if "Gateway" in diff:
            return "PASS"
        return "FAIL - Evidence not found in diff."