"""Regression checks for tool boundaries and real verification."""
from pathlib import Path
import sys
import pytest

MODULE = Path(__file__).resolve().parent
sys.path.insert(0, str(MODULE.parent))
sys.path.insert(0, str(MODULE))
from demo_tools import DemoTools
from shared.agent import run_agent
from shared.demo_project import create_workspace


def test_demo_reproduces_failure_and_verifies_repair():
    tools = DemoTools(create_workspace())
    tests = tools.read_file('tests/test_checkout.py')
    baseline = tools.run_tests()
    assert baseline['returncode'] == 1
    assert '1 failed, 4 passed' in baseline['output']
    source = tools.read_file('src/checkout.py')
    tools.write_file('src/checkout.py', source.replace(
        'subtotal - discount_percent',
        'subtotal * (1 - discount_percent / 100)'))
    final = tools.run_tests()
    assert final['returncode'] == 0
    assert '5 passed' in final['output']
    assert tools.read_file('tests/test_checkout.py') == tests


def test_only_implementation_is_writable():
    tools = DemoTools(create_workspace())
    for path in ('tests/test_checkout.py', 'src/__init__.py',
                 'CONTRIBUTING.md', '../escape.py'):
        with pytest.raises(PermissionError):
            tools.write_file(path, 'invalid')


def test_agent_reports_rejected_test_edit_via_callback():
    class FakeClient:
        calls = 0

        def chat(self, messages, tools):
            self.calls += 1
            if self.calls == 1:
                return {'role': 'assistant', 'content': '', 'tool_calls': [
                    {'function': {'name': 'write_file', 'arguments': {
                        'path': 'tests/test_checkout.py', 'content': ''}}}]}
            return {'role': 'assistant', 'content': 'Blocked.'}

    tools = DemoTools(create_workspace())
    original = tools.read_file('tests/test_checkout.py')
    events = []
    result = run_agent(FakeClient(), tools, 'Attempt edit', on_event=events.append)
    assert events == result['events']
    assert events[1]['result']['error'] == 'PermissionError'
    assert tools.read_file('tests/test_checkout.py') == original
