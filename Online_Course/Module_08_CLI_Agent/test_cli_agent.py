from cli_agent import DemoAgent, State

def test_agent_fixes_and_verifies():
    s = State("fix", {"checkout.py": "total = subtotal - discount_percent"})
    out = DemoAgent().run(s)
    assert out.tests_pass
    assert out.history[-1] == "stop:goal-met"
