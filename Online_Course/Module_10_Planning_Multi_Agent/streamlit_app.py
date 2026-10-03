from pathlib import Path
import sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
import streamlit as st
from shared.streamlit_common import client_panel
from shared.demo_project import CHECKOUT
from shared.multi_agent import run_team
st.set_page_config(page_title="Module 10 · Multi-Agent",layout="wide"); st.title("Module 10 · Planning and Multi-Agent Systems")
client=client_panel(); goal=st.text_input("Engineering goal","Add coupon support while preserving percentage discounts")
if st.button("Run Planner → Coder → Tester → Reviewer"):
    result=run_team(client,goal,CHECKOUT)
    for role,text in result.items(): st.subheader(role.title()); st.markdown(text)
st.info("Each role is a separate Ollama inference. Later orchestration modules add tool execution and verification.")
