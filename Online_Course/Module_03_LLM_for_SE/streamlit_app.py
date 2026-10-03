import streamlit as st
st.set_page_config(page_title="Module 3 · LLMs for SE",layout="wide"); st.title("Module 3 · LLMs for Software Engineering")
st.info("Use AI for coding, debugging, tests, review, and documentation, but verify the output.")
raw=st.text_input("Username input","  Alice.Smith  "); st.code("def normalize_username(value):\n    return value.strip()",language="python"); st.error(f"Current: {raw.strip()!r} · expected normalized lowercase")
if st.button("Apply repair"): st.code("return value.strip().lower()",language="python"); st.success(f"Verified example output: {raw.strip().lower()!r}")
