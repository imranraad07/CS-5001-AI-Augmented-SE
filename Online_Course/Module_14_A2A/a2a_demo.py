"""Module 14: dependency-free model of structured agent-to-agent messages.

This is a teaching model, not an implementation of a particular A2A SDK/protocol.
"""
from dataclasses import dataclass, asdict
import json

@dataclass(frozen=True)
class AgentMessage:
    sender: str
    recipient: str
    task: str
    context: dict
    status: str = "request"

    def to_json(self) -> str:
        return json.dumps(asdict(self), sort_keys=True)

def planner_message() -> AgentMessage:
    return AgentMessage(
        sender="planner",
        recipient="coder",
        task="Fix percentage discount without changing tests",
        context={"file": "checkout.py", "verification": "run_tests"},
    )

def coder_result(request: AgentMessage) -> AgentMessage:
    return AgentMessage(
        sender="coder",
        recipient="reviewer",
        task="Review proposed checkout change",
        context={"change": "subtotal * (1 - discount_percent / 100)", "tests": {"passed": 5, "failed": 0}},
        status="result",
    )

if __name__ == "__main__":
    request = planner_message()
    print(request.to_json())
    print(coder_result(request).to_json())
