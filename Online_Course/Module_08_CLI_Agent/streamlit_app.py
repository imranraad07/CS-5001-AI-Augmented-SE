from pathlib import Path
import sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
import streamlit as st
from shared.streamlit_common import client_panel
from shared.demo_project import create_workspace
from shared.repo_tools import RepoTools
from shared.agent import run_agent
st.set_page_config(page_title="Module 8 · AI Agent",layout="wide"); st.title("Module 8 · From LLM to AI Agent")
client=client_panel()
if "ws8" not in st.session_state: st.session_state.ws8=str(create_workspace())
tools=RepoTools(st.session_state.ws8); goal=st.text_area("Goal","Fix the failing checkout test without modifying tests. Verify your work."); steps=st.slider("Max agent steps",2,12,8)
if st.button("Run real tool-calling agent"):
    result=run_agent(client,tools,goal,steps)
    for e in result["events"]: st.json(e)
    st.subheader("Actual audit log"); st.json(tools.audit); st.subheader("Actual pytest"); st.code(tools.run_tests()["output"])
if st.button("Reset",key="r8"): st.session_state.ws8=str(create_workspace()); st.rerun()
