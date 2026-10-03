import streamlit as st
st.set_page_config(page_title="Module 5 · Prompt Patterns",layout="wide"); st.title("Module 5 · Prompt Patterns and Decomposition")
incident=st.text_area("Incident","Users intermittently receive Nginx 502 responses."); p=st.selectbox("Pattern",["Persona","Flipped Interaction","Question Refinement","Cognitive Verifier","Reflection"])
m={"Persona":"Act as an SRE. Diagnose from observable evidence.","Flipped Interaction":"Ask one diagnostic question at a time until enough evidence exists.","Question Refinement":"Rewrite this as a precise debugging question and identify missing information.","Cognitive Verifier":"Check reproduce → classify → hypothesize → validate → fix.","Reflection":"Identify unsupported assumptions in the proposed diagnosis and request evidence."}
st.code(m[p]+"\n\nIncident: "+incident); st.info("Decompose: observe → classify → hypothesize → validate → fix → verify")
