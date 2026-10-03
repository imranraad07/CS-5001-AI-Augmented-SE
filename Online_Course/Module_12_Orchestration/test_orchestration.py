from orchestration import Orchestrator, WorkflowState

def test_orchestrator_retries_then_finishes():
    out = Orchestrator().run(WorkflowState("fix", "total = subtotal - discount_percent"))
    assert "orchestrator:retry" in out.events
    assert out.events[-1] == "orchestrator:finish"
    assert out.review == "approved"
