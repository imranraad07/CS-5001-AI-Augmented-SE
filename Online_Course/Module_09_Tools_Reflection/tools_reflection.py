"""Module 9: controlled tools plus producer/critic reflection."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Tool:
    name: str
    description: str

TOOLS = {
    "read_file": Tool("read_file", "Read a repository file"),
    "edit_file": Tool("edit_file", "Replace an approved code fragment"),
    "run_tests": Tool("run_tests", "Run verification tests"),
}

def producer(code: str, attempt: int) -> str:
    if attempt == 1:
        return code.replace("subtotal - discount_percent", "subtotal - (discount_percent / 100)")
    return code.replace("subtotal - discount_percent", "subtotal * (1 - discount_percent / 100)")

def run_tests(code: str) -> tuple[bool, str]:
    ok = "subtotal * (1 - discount_percent / 100)" in code
    return ok, "5 passed" if ok else "1 failed, 4 passed"

def critic(test_output: str) -> str:
    return "accept" if "5 passed" in test_output else "revise: implementation still violates percentage semantics"

def demo() -> None:
    original = "total = subtotal - discount_percent"
    for attempt in (1, 2):
        candidate = producer(original, attempt)
        passed, output = run_tests(candidate)
        print(f"attempt {attempt}: {candidate}")
        print("tests:", output)
        print("critic:", critic(output))
        if passed:
            break

if __name__ == "__main__":
    demo()
