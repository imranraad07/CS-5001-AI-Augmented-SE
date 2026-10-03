"""Module 13: MCP concepts represented as local structured schemas/messages.

This is NOT an MCP protocol implementation. It is a dependency-free teaching model
of the client/server/tool-schema concepts from the lecture.
"""
from dataclasses import dataclass
from typing import Any, Callable

@dataclass(frozen=True)
class ToolSchema:
    name: str
    description: str
    parameters: dict[str, str]
    output: str

class DemoMCPServer:
    def __init__(self):
        self.schemas = {
            "search_repo": ToolSchema("search_repo", "Search repository files", {"query": "string"}, "list[string]"),
            "run_tests": ToolSchema("run_tests", "Run repository tests", {"path": "string"}, "object"),
        }
        self.handlers: dict[str, Callable[..., Any]] = {
            "search_repo": lambda query: ["src/checkout.py"] if "checkout" in query.lower() else [],
            "run_tests": lambda path: {"passed": 5, "failed": 0, "path": path},
        }

    def list_tools(self) -> list[ToolSchema]:
        return list(self.schemas.values())

    def call_tool(self, name: str, arguments: dict) -> Any:
        if name not in self.handlers:
            raise KeyError(name)
        return self.handlers[name](**arguments)

if __name__ == "__main__":
    server = DemoMCPServer()
    for schema in server.list_tools():
        print(schema)
    print(server.call_tool("run_tests", {"path": "/repo"}))
