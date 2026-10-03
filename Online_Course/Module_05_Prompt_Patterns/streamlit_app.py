from pathlib import Path
import sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
import streamlit as st
from shared.streamlit_common import client_panel
st.set_page_config(page_title="Module 5 · Prompt Patterns",layout="wide"); st.title("Module 5 · Prompt Patterns and Decomposition")
client=client_panel(); incident=st.text_area("Incident","Users intermittently receive Nginx 502 responses.")
patterns={"Persona":"Act as an SRE. Diagnose using observable evidence before proposing changes.","Flipped Interaction":"Ask one diagnostic question at a time; do not diagnose until enough evidence exists.","Question Refinement":"Rewrite the incident as a precise debugging question and identify missing information.","Cognitive Verifier":"Decompose into observable failure, failure mode, hypothesis, validation, fix, verification.","Reflection":"Propose a diagnosis, then critique unsupported assumptions and request evidence."}
p=st.selectbox("Pattern",list(patterns))
if st.button("Execute with Ollama"): st.markdown(client.generate(patterns[p]+"\n\nINCIDENT:\n"+incident))
