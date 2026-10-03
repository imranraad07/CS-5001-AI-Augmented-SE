"""Module 12: explicit orchestration, routing, verification, and retry."""
from dataclasses import dataclass, field

@dataclass
class WorkflowState:
    goal: str
    artifact: str
    attempts: int = 0
    tests_pass: bool = False
    review: str = "pending"
    events: list[str] = field(default_factory=list)

class Orchestrator:
    def __init__(self, max_attempts: int = 2):
        self.max_attempts = max_attempts

    def run(self, state: WorkflowState) -> WorkflowState:
        state.events.append("planner:inspect")
        while state.attempts < self.max_attempts:
            state.attempts += 1
            state.events.append(f"coder:attempt-{state.attempts}")
            if state.attempts == 1:
                candidate = state.artifact.replace("subtotal - discount_percent", "subtotal - discount_percent / 100")
            else:
                candidate = state.artifact.replace("subtotal - discount_percent", "subtotal * (1 - discount_percent / 100)")
            state.events.append("tester:run")
            state.tests_pass = "subtotal * (1 - discount_percent / 100)" in candidate
            if not state.tests_pass:
                state.events.append("orchestrator:retry")
                continue
            state.artifact = candidate
            state.events.append("reviewer:review")
            state.review = "approved"
            state.events.append("orchestrator:finish")
            return state
        state.events.append("orchestrator:escalate")
        return state

if __name__ == "__main__":
    s = WorkflowState("fix checkout", "total = subtotal - discount_percent")
    out = Orchestrator().run(s)
    print("\n".join(out.events))
