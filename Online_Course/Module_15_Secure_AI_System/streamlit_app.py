from pathlib import Path
import sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
import streamlit as st
from shared.streamlit_common import client_panel
from shared.demo_project import create_workspace
from shared.repo_tools import RepoTools
from shared.agent import run_agent
st.set_page_config(page_title="Module 15 · Controlled AI System",layout="wide"); st.title("Module 15 · Engineering a Controlled AI-Augmented SE System")
client=client_panel()
if "ws15" not in st.session_state: st.session_state.ws15=str(create_workspace())
tools=RepoTools(st.session_state.ws15); goal=st.text_area("Goal","Fix the checkout defect, preserve tests, use only repository tools, and verify the result."); limit=st.slider("Agent action/decision limit",2,12,8)
if st.button("Execute controlled system"):
    result=run_agent(client,tools,goal,limit)
    st.subheader("Agent/tool trace"); [st.json(e) for e in result["events"]]
    st.subheader("Audit log"); st.json(tools.audit)
    verification=tools.run_tests(); st.subheader("Independent final verification"); st.code(verification["output"])
    if verification["returncode"]==0: st.success("Verified")
    else: st.error("Not verified; human review/escalation required")
