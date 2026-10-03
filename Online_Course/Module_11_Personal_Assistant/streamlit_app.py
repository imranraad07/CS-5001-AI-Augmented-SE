import streamlit as st
st.set_page_config(page_title="Module 11 · Personal Assistant",layout="wide"); st.title("Module 11 · Building a Personalized AI Assistant")
st.warning("Controlled-controller demo. No arbitrary shell or HTTP execution is performed.")
cmd=st.selectbox("Capability",["write_note","read_note","arbitrary_shell"]); arg=st.text_input("Argument","Review checkout tests")
if st.button("Request action"):
    if cmd=="arbitrary_shell": st.error("DENIED: capability is not allowlisted.")
    else: st.success("AUTHORIZED"); st.code(f"AUDIT command={cmd!r} argument={arg!r}")
st.info("LLM → controller → validated, predefined capabilities → audit")
