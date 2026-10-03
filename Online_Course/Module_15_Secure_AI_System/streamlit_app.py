import streamlit as st
st.set_page_config(page_title="Module 15 · Secure System",layout="wide"); st.title("Module 15 · Security, Responsible Use, and the Complete System")
cap=st.selectbox("Requested capability",["read_file","run_tests","arbitrary_shell","external_http"]); used=st.slider("Actions used",0,5,1); limit=3; allowed={"read_file","run_tests"}
a,b=st.columns(2); a.metric("Budget",f"{used}/{limit}"); b.metric("Allowlisted","Yes" if cap in allowed else "No")
if st.button("Authorize"):
    if used>=limit: st.error("DENIED: action budget exhausted. Escalate.")
    elif cap not in allowed: st.error("DENIED: capability not allowlisted.")
    else: st.success("AUTHORIZED: validate → execute within boundary → audit → verify")
st.code("User → Prompt/Plan → RAG → Agent/Orchestrator → Controlled Tools → Verification → Audit/Human Oversight")
