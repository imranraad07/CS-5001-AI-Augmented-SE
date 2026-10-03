"""Module 10: planning and specialized logical agents."""
from dataclasses import dataclass

@dataclass
class Task:
    name: str
    owner: str
    status: str = "pending"

class Planner:
    def plan(self, goal: str) -> list[Task]:
        return [
            Task("inspect requirements", "requirements"),
            Task("implement minimum change", "coder"),
            Task("run regression tests", "tester"),
            Task("review behavior and interfaces", "reviewer"),
        ]

class Coder:
    def run(self, artifact: str) -> str:
        return artifact.replace("subtotal - discount_percent", "subtotal * (1 - discount_percent / 100)")

class Tester:
    def run(self, artifact: str) -> dict:
        passed = "subtotal * (1 - discount_percent / 100)" in artifact
        return {"passed": 5 if passed else 4, "failed": 0 if passed else 1}

class Reviewer:
    def run(self, artifact: str, tests: dict) -> str:
        return "approved" if tests["failed"] == 0 and "discount_percent / 100" in artifact else "changes_requested"

def demo() -> None:
    plan = Planner().plan("Fix checkout discount and verify behavior")
    for task in plan:
        print(f"{task.owner:12} -> {task.name}")
    code = Coder().run("total = subtotal - discount_percent")
    tests = Tester().run(code)
    print("tests:", tests)
    print("review:", Reviewer().run(code, tests))

if __name__ == "__main__":
    demo()
