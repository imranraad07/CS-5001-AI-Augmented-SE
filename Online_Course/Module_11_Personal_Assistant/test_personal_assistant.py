from pathlib import Path
import pytest
from personal_assistant import Controller

def test_allowed_commands_and_audit(tmp_path: Path):
    c = Controller(tmp_path)
    c.execute("write_note", relative="x.txt", text="hello")
    assert c.execute("read_note", relative="x.txt") == "hello"
    assert len(c.audit) == 2

def test_rejects_unknown_command(tmp_path: Path):
    with pytest.raises(PermissionError):
        Controller(tmp_path).execute("shell", command_line="rm -rf /")

def test_rejects_path_escape(tmp_path: Path):
    with pytest.raises(PermissionError):
        Controller(tmp_path).execute("write_note", relative="../outside.txt", text="no")
