import streamlit as st
st.set_page_config(page_title="Module 14 · A2A",layout="wide"); st.title("Module 14 · A2A and Agentic Protocols")
st.warning("Conceptual teaching simulation. It does not claim conformance with a specific current A2A SDK/version.")
sender=st.selectbox("Sender",["Planner","Coder","Tester","Reviewer"]); receiver=st.selectbox("Receiver",["Coder","Tester","Reviewer","Planner"]); task=st.text_input("Task","Fix failing percentage-discount test")
if st.button("Send message"): st.json({"from":sender,"to":receiver,"type":"task_request","task":task,"context":{"repo":"checkout-demo"},"expected_result":"structured status"})
st.info("Tool interaction: Agent → MCP → Tool. Agent communication: Agent → A2A → Agent.")
