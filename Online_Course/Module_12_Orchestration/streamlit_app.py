from pathlib import Path
import sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
import streamlit as st
from shared.streamlit_common import client_panel
from shared.demo_project import create_workspace
from shared.repo_tools import RepoTools
from shared.orchestration import orchestrate
st.set_page_config(page_title="Module 12 · Orchestration",layout="wide"); st.title("Module 12 · AI Agent Orchestration")
client=client_panel()
if "ws12" not in st.session_state: st.session_state.ws12=str(create_workspace())
tools=RepoTools(st.session_state.ws12); retries=st.slider("Retry budget",0,3,1)
if st.button("Run orchestrated fix"):
    result=orchestrate(client,tools,"Fix the percentage-discount defect. Preserve tests and verify the implementation.",retries)
    st.write("Workflow status:",result["status"])
    for a in result["attempts"]: st.subheader(f"Attempt {a['attempt']}"); st.code(a["verification"]["output"]); st.json(a["agent"]["events"])
