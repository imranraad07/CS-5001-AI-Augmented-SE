from mcp_demo import DemoMCPServer

def test_tools_have_structured_schemas():
    tools = DemoMCPServer().list_tools()
    assert {t.name for t in tools} == {"search_repo", "run_tests"}
    assert all(t.parameters and t.output for t in tools)

def test_structured_tool_call():
    result = DemoMCPServer().call_tool("run_tests", {"path": "/repo"})
    assert result == {"passed": 5, "failed": 0, "path": "/repo"}
