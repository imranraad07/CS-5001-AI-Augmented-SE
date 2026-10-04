from pathlib import Path
import sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
import streamlit as st
from shared.streamlit_common import client_panel
from shared.demo_project import create_workspace
from shared.repo_tools import RepoTools
from shared.agent import run_agent
st.set_page_config(page_title="Module 9 · Tools and Reflection",layout="wide"); st.title("Module 9 · Tool Use and Reflection")
client=client_panel()
if "ws9" not in st.session_state: st.session_state.ws9=str(create_workspace())
tools=RepoTools(st.session_state.ws9)
if st.button("Run agent and inspect tool feedback"):
    result=run_agent(client,tools,"Diagnose and fix the failing test. Inspect evidence, use tools, run pytest after editing, and reflect on failures before retrying.",10)
    for e in result["events"]:
        if e["type"]=="tool": st.write("OBSERVATION FROM REAL TOOL"); st.json(e)
        else: st.write("MODEL DECISION"); st.json(e)
    st.code(tools.run_tests()["output"])
if st.button("Reset",key="r9"): st.session_state.ws9=str(create_workspace()); st.rerun()
