import streamlit as st
st.set_page_config(page_title="Module 10 · Multi-Agent",layout="wide"); st.title("Module 10 · Planning and Multi-Agent Systems")
goal=st.text_input("Engineering goal","Add coupon support to checkout")
if st.button("Plan and delegate"):
    for role,task in [("Planner","Clarify requirements and affected interfaces"),("Coder","Implement minimal change"),("Tester","Create/run behavioral tests"),("Reviewer","Review interfaces, edge cases, evidence")]: st.write(f"**{role} →** {task}")
    st.success("Specialized roles coordinated around: "+goal)
