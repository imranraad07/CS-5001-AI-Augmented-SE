from pathlib import Path
import sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
import streamlit as st
from shared.streamlit_common import client_panel
st.set_page_config(page_title="Module 2 · LLM Basics",layout="wide"); st.title("Module 2 · How LLMs Work")
client=client_panel(); context=st.text_area("Context","items = ['a', 'b', 'c']\nfor i in range(")
if st.button("Generate continuation with local model"): st.code(client.generate("Continue with only a short likely continuation:\n\n"+context))
st.info("Change the context and rerun. This output comes from the configured Ollama model.")
