from pathlib import Path
import sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
import streamlit as st
from shared.streamlit_common import client_panel
from shared.demo_project import create_workspace
from Module_13_MCP.mcp_client import call_sync
st.set_page_config(page_title="Module 13 · MCP",layout="wide"); st.title("Module 13 · MCP: Connecting Agents to Tools")
st.caption("This starts a real MCP stdio server/client session using the installed MCP Python SDK.")
if "ws13" not in st.session_state: st.session_state.ws13=str(create_workspace())
tool=st.selectbox("MCP tool",["run_tests","read_file","search_repo"]); args={}
if tool=="read_file": args={"path":st.text_input("Path","src/checkout.py")}
elif tool=="search_repo": args={"query":st.text_input("Query","discount")}
if st.button("Discover and call through MCP"):
    listed,result=call_sync(st.session_state.ws13,tool,args)
    st.subheader("Discovered MCP tools"); st.write([t.name for t in listed.tools])
    st.subheader("MCP call result"); st.write(result)
