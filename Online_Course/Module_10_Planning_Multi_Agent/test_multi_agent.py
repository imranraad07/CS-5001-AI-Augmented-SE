from multi_agent import Coder, Planner, Reviewer, Tester

def test_plan_has_specialized_roles():
    assert [t.owner for t in Planner().plan("goal")] == ["requirements", "coder", "tester", "reviewer"]

def test_pipeline_reaches_approval():
    code = Coder().run("total = subtotal - discount_percent")
    tests = Tester().run(code)
    assert Reviewer().run(code, tests) == "approved"
