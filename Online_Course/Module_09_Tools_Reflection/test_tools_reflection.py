from tools_reflection import TOOLS, critic, producer, run_tests

def test_tool_registry_is_explicit():
    assert set(TOOLS) == {"read_file", "edit_file", "run_tests"}

def test_reflection_revises_failure():
    candidate = producer("total = subtotal - discount_percent", 1)
    _, output = run_tests(candidate)
    assert critic(output).startswith("revise")
