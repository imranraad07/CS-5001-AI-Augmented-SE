"""MCP stdio client used by the Streamlit demonstration."""
from __future__ import annotations
import asyncio, os, sys
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def call(workspace,tool_name,arguments=None):
    server=Path(__file__).with_name("mcp_server.py")
    params=StdioServerParameters(command=sys.executable,args=[str(server)],env={**os.environ,"CS5001_WORKSPACE":str(workspace)})
    async with stdio_client(params) as (read,write):
        async with ClientSession(read,write) as session:
            await session.initialize()
            listed=await session.list_tools()
            result=await session.call_tool(tool_name,arguments or {})
            return listed,result

def call_sync(workspace,tool_name,arguments=None):
    return asyncio.run(call(workspace,tool_name,arguments))
