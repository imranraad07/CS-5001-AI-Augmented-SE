from pathlib import Path
import pytest
from secure_system import SecureController

def test_allowlisted_read_and_audit(tmp_path: Path):
    (tmp_path / "x.txt").write_text("safe", encoding="utf-8")
    c = SecureController(tmp_path)
    assert c.execute("read_file", {"path": "x.txt"}) == "safe"
    assert c.audit.events[-1]["status"] == "ok"

def test_denies_unlisted_tool(tmp_path: Path):
    with pytest.raises(PermissionError):
        SecureController(tmp_path).execute("shell", {"path": "x"})

def test_action_limit(tmp_path: Path):
    (tmp_path / "x.txt").write_text("safe", encoding="utf-8")
    c = SecureController(tmp_path, max_actions=1)
    c.execute("read_file", {"path": "x.txt"})
    with pytest.raises(RuntimeError):
        c.execute("read_file", {"path": "x.txt"})
