from pathlib import Path
import sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
import streamlit as st
from shared.streamlit_common import client_panel
from shared.demo_project import DOCS
from shared.rag import RAG
st.set_page_config(page_title="Module 6 · RAG",layout="wide"); st.title("Module 6 · RAG: Giving AI Project Knowledge")
client=client_panel(); q=st.text_input("Project question","What checks are required before merge?"); k=st.slider("Top-k",1,3,2)
if st.button("Retrieve with Ollama embeddings and answer"):
    rag=RAG(client,DOCS); answer,hits=rag.answer(q,k)
    st.subheader("Actual retrieved chunks")
    for i,h in enumerate(hits,1): st.write(f"[S{i}] {h['source']} · cosine={h['score']:.3f}"); st.code(h["text"])
    st.subheader("Grounded Ollama answer"); st.markdown(answer)
