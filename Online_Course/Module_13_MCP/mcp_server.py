"""Real MCP server exposing bounded software-engineering tools."""
from pathlib import Path
import os, sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
from mcp.server.fastmcp import FastMCP
from shared.repo_tools import RepoTools

ROOT=Path(os.environ.get("CS5001_WORKSPACE",".")).resolve()
tools=RepoTools(ROOT)
mcp=FastMCP("CS5001 Software Engineering Tools")

@mcp.tool()
def read_file(path:str)->str:
    """Read a file inside the configured workspace."""
    return tools.read_file(path)

@mcp.tool()
def search_repo(query:str)->list[str]:
    """Search repository text inside the configured workspace."""
    return tools.search_repo(query)

@mcp.tool()
def run_tests()->dict:
    """Run pytest inside the configured workspace."""
    return tools.run_tests()

if __name__=="__main__":
    mcp.run()
