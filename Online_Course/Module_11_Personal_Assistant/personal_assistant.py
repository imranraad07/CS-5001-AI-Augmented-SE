"""Module 11: local assistant controller with an allowlisted capability set."""
from pathlib import Path

class Controller:
    def __init__(self, workspace: Path):
        self.workspace = workspace.resolve()
        self.workspace.mkdir(parents=True, exist_ok=True)
        self.audit: list[str] = []

    def _safe_path(self, relative: str) -> Path:
        candidate = (self.workspace / relative).resolve()
        if self.workspace not in candidate.parents and candidate != self.workspace:
            raise PermissionError("path escapes workspace")
        return candidate

    def write_note(self, relative: str, text: str) -> str:
        path = self._safe_path(relative)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        self.audit.append(f"write_note:{relative}")
        return str(path)

    def read_note(self, relative: str) -> str:
        text = self._safe_path(relative).read_text(encoding="utf-8")
        self.audit.append(f"read_note:{relative}")
        return text

    def execute(self, command: str, **args):
        allowed = {"write_note": self.write_note, "read_note": self.read_note}
        if command not in allowed:
            raise PermissionError(f"command not allowed: {command}")
        return allowed[command](**args)

if __name__ == "__main__":
    controller = Controller(Path("demo_workspace"))
    controller.execute("write_note", relative="notes/todo.txt", text="Run tests before commit.")
    print(controller.execute("read_note", relative="notes/todo.txt"))
    print("audit:", controller.audit)
