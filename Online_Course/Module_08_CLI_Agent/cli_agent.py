"""Module 8: deterministic CLI software-engineering agent control loop."""
from dataclasses import dataclass, field

@dataclass
class State:
    goal: str
    files: dict[str, str]
    tests_pass: bool = False
    history: list[str] = field(default_factory=list)

class DemoAgent:
    def __init__(self, max_iterations: int = 4):
        self.max_iterations = max_iterations

    def observe(self, state: State) -> str:
        state.history.append("observe")
        return state.files["checkout.py"]

    def decide(self, state: State, observation: str) -> str:
        state.history.append("decide")
        if "subtotal - discount_percent" in observation:
            return "edit"
        return "verify"

    def act(self, state: State, action: str) -> None:
        state.history.append(f"act:{action}")
        if action == "edit":
            state.files["checkout.py"] = state.files["checkout.py"].replace(
                "subtotal - discount_percent",
                "subtotal * (1 - discount_percent / 100)",
            )

    def evaluate(self, state: State) -> bool:
        state.history.append("evaluate")
        state.tests_pass = "subtotal * (1 - discount_percent / 100)" in state.files["checkout.py"]
        return state.tests_pass

    def run(self, state: State) -> State:
        for _ in range(self.max_iterations):
            observation = self.observe(state)
            self.act(state, self.decide(state, observation))
            if self.evaluate(state):
                state.history.append("stop:goal-met")
                return state
            state.history.append("reflect")
        state.history.append("stop:max-iterations")
        return state

if __name__ == "__main__":
    state = State("Fix percentage discount", {"checkout.py": "total = subtotal - discount_percent"})
    result = DemoAgent().run(state)
    print("\n".join(result.history))
    print(result.files["checkout.py"])
