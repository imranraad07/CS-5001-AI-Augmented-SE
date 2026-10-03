from pathlib import Path
import sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
import streamlit as st
from shared.streamlit_common import client_panel
from shared.demo_project import create_workspace
from shared.repo_tools import RepoTools
from shared.agent import run_agent
st.set_page_config(page_title="Module 1 · AI-Augmented SE",layout="wide"); st.title("Module 1 · AI-Augmented Software Engineering Crash Course")
client=client_panel()
if "ws1" not in st.session_state: st.session_state.ws1=str(create_workspace())
tools=RepoTools(st.session_state.ws1)
st.subheader("Real demo repository"); st.code(tools.read_file("src/checkout.py"),language="python")
if st.button("Run real baseline pytest"): r=tools.run_tests(); st.code(r["output"])
goal=st.text_area("Agent goal","Fix the failing percentage-discount behavior. Do not modify tests. Make the minimum implementation change and verify it.")
if st.button("Run Ollama software-engineering agent"):
    result=run_agent(client,tools,goal)
    for e in result["events"]:
        if e["type"]=="tool": st.write("TOOL",e["name"],e["arguments"]); st.json(e["result"] if isinstance(e["result"],dict) else {"result":e["result"]})
        elif e.get("content"): st.write("AGENT",e["content"])
    st.code(tools.read_file("src/checkout.py"),language="python"); final=tools.run_tests(); st.code(final["output"]); st.success("Verified by pytest" if final["returncode"]==0 else "Not verified")
if st.button("Reset disposable repository"): st.session_state.ws1=str(create_workspace()); st.rerun()
