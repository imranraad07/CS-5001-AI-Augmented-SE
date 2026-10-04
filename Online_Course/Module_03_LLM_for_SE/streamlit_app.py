from pathlib import Path
import sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
import streamlit as st
from shared.streamlit_common import client_panel
from shared.demo_project import create_workspace
from shared.repo_tools import RepoTools
st.set_page_config(page_title="Module 3 · LLMs for SE",layout="wide"); st.title("Module 3 · LLMs for Software Engineering")
client=client_panel()
if "ws3" not in st.session_state: st.session_state.ws3=str(create_workspace())
tools=RepoTools(st.session_state.ws3); code=tools.read_file("src/checkout.py"); tests=tools.run_tests()
st.code(code,language="python"); st.code(tests["output"])
task=st.selectbox("Actual LLM task",["Debug the failure","Propose a minimal repair","Generate edge-case tests","Review the code","Write documentation"])
if st.button("Run with Ollama"): st.markdown(client.generate(f"Task: {task}\n\nCODE:\n{code}\n\nREAL PYTEST OUTPUT:\n{tests['output']}\nDistinguish proposals from verified facts.",system="You are an AI pair programmer."))
