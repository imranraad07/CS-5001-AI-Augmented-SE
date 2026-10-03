import streamlit as st
st.set_page_config(page_title="Module 13 · MCP",layout="wide"); st.title("Module 13 · MCP: Connecting Agents to Tools")
st.warning("Conceptual teaching simulation. This is not presented as a conforming implementation of a current MCP SDK.")
tool=st.selectbox("Exposed tool",["search_repo","run_tests"]); schemas={"search_repo":{"query":"string","path":"optional string"},"run_tests":{"path":"string"}}; st.json({"name":tool,"parameters":schemas[tool],"output":"structured result"})
if st.button("Call tool"): st.json({"tool":tool,"result":{"passed":5,"failed":0}} if tool=="run_tests" else {"tool":tool,"result":["src/checkout.py","tests/test_checkout.py"]})
st.info("Prompting guides reasoning · RAG retrieves knowledge · tool calling acts · MCP standardizes the tool interface.")
