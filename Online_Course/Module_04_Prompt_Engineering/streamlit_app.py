import streamlit as st
st.set_page_config(page_title="Module 4 · Prompt Engineering",layout="wide"); st.title("Module 4 · Prompt Engineering for Software Engineers")
task=st.text_input("Task","Fix the checkout bug"); a,b=st.columns(2); a.subheader("Weak"); a.code("Fix this code.")
b.subheader("Engineered"); b.code(f"""CONTEXT: Python checkout project; percentage-discount test fails.
TASK: {task}
CONSTRAINTS: Preserve interfaces; do not modify tests; no dependencies; minimum change.
EXPECTED OUTPUT: Explain failure, patch, verification.
VERIFICATION: Run tests.""")
