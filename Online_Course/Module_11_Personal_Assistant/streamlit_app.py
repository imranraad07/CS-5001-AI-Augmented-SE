from pathlib import Path
import sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
import streamlit as st
from shared.streamlit_common import client_panel
from shared.demo_project import create_workspace
from shared.repo_tools import RepoTools
from shared.agent import run_agent
st.set_page_config(page_title="Module 11 · Personalized Assistant",layout="wide"); st.title("Module 11 · Building a Controlled Personalized AI Assistant")
client=client_panel()
if "ws11" not in st.session_state: st.session_state.ws11=str(create_workspace())
tools=RepoTools(st.session_state.ws11); request=st.text_area("Request","Inspect the checkout implementation and tell me whether the tests pass. Do not change files.")
if st.button("Run controlled assistant"):
    result=run_agent(client,tools,request,5)
    for e in result["events"]: st.json(e)
    st.subheader("Controller audit"); st.json(tools.audit)
st.info("The model can only access allowlisted repository tools inside the disposable workspace boundary.")
