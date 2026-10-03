import streamlit as st
st.set_page_config(page_title="Module 2 · LLM Basics",layout="wide"); st.title("Module 2 · How LLMs Work")
st.warning("Teaching simulation: probabilities are illustrative, not measurements from a real LLM.")
context=st.selectbox("Context",["Mary had a little","for i in range(","items = ['a', 'b', 'c']\nfor i in range("])
data={"Mary had a little":{"lamb":.78,"girl":.08,"house":.06,"dog":.04,"car":.04},"for i in range(":{"10":.40,"len(items)":.25,"n":.20,"100":.10,"x":.05},"items = ['a', 'b', 'c']\nfor i in range(":{"len(items)":.65,"3":.20,"10":.08,"n":.05,"x":.02}}[context]
st.bar_chart(data); st.code(context+max(data,key=data.get)); st.info("Changing context changes the next-token distribution.")
