"""Module 15: consolidate course controls around an AI-triggered capability layer."""
from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class AuditLog:
    events: list[dict] = field(default_factory=list)
    def record(self, **event) -> None:
        self.events.append(event)

class SecureController:
    def __init__(self, workspace: Path, max_actions: int = 3):
        self.workspace = workspace.resolve()
        self.workspace.mkdir(parents=True, exist_ok=True)
        self.max_actions = max_actions
        self.actions = 0
        self.audit = AuditLog()

    def _consume_budget(self):
        if self.actions >= self.max_actions:
            raise RuntimeError("action limit reached")
        self.actions += 1

    def _path(self, relative: str) -> Path:
        p = (self.workspace / relative).resolve()
        if self.workspace not in p.parents and p != self.workspace:
            raise PermissionError("workspace boundary violation")
        return p

    def execute(self, tool: str, arguments: dict):
        self._consume_budget()
        if tool != "read_file":
            self.audit.record(tool=tool, status="denied")
            raise PermissionError("tool not allowlisted")
        if set(arguments) != {"path"} or not isinstance(arguments["path"], str):
            raise ValueError("invalid arguments")
        path = self._path(arguments["path"])
        result = path.read_text(encoding="utf-8")
        self.audit.record(tool=tool, path=arguments["path"], status="ok")
        return result

if __name__ == "__main__":
    workspace = Path("secure_workspace")
    workspace.mkdir(exist_ok=True)
    (workspace / "README.txt").write_text("Verify AI output before accepting changes.", encoding="utf-8")
    controller = SecureController(workspace)
    print(controller.execute("read_file", {"path": "README.txt"}))
    print(controller.audit.events)
