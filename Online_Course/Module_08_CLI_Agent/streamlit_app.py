import streamlit as st
st.set_page_config(page_title="Module 8 · AI Agent",layout="wide"); st.title("Module 8 · From LLM to AI Agent")
st.warning("Deterministic agent simulation: the decision policy stands in for an LLM for reproducible teaching.")
st.slider("Max iterations",1,5,3)
if st.button("Run agent"):
    for phase,msg in [("Observe","1 percentage test fails"),("Decide","Inspect calculation"),("Act","Apply percentage formula"),("Evaluate","5 tests pass"),("Reflect","Goal verified; stop")]: st.write(f"**{phase}:** {msg}")
st.info("Agent loop: Observe → Decide → Act → Evaluate → Reflect → Retry/Stop")
