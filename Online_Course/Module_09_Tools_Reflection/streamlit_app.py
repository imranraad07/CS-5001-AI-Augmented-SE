import streamlit as st
st.set_page_config(page_title="Module 9 · Tools & Reflection",layout="wide"); st.title("Module 9 · Tool Use and Reflection")
st.code("Tools: read_file · edit_file · run_tests"); attempt=st.radio("Attempt",[1,2],horizontal=True)
if attempt==1: st.code("total = subtotal - discount_percent",language="python"); st.error("run_tests: 1 failed, 4 passed"); st.info("Critique: percentage is being treated as currency. Revise.")
else: st.code("total = subtotal * (1 - discount_percent / 100)",language="python"); st.success("run_tests: 5 passed"); st.info("Reflection: verification passed. Stop.")
