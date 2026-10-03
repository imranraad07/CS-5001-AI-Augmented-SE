import streamlit as st
st.set_page_config(page_title="Module 6 · RAG",layout="wide"); st.title("Module 6 · RAG: Giving AI Project Knowledge")
st.warning("Teaching implementation: keyword retrieval and grounded response behavior, not an external LLM.")
docs={"CONTRIBUTING.md":"Before merge, run unit tests and lint checks. Do not bypass failing tests.","RUNBOOK.md":"For checkout incidents, inspect logs and reproduce the failure before deployment.","OWNERS.md":"Checkout changes require review from payments maintainers."}
tok=lambda s:set(x.strip(".,:;!?").lower() for x in s.split()); q=st.text_input("Question","What checks are required before merge?"); ranked=sorted(docs.items(),key=lambda x:len(tok(q)&tok(x[1])),reverse=True); k=st.slider("Top-k",1,3,2)
for n,t in ranked[:k]: st.write("**"+n+"**"); st.code(t)
if st.button("Generate grounded response"): st.success("Answer using only the retrieved evidence and cite: "+", ".join(n for n,_ in ranked[:k]))
