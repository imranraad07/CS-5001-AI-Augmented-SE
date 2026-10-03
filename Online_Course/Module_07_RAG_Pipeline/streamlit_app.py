from pathlib import Path
import sys
COURSE=Path(__file__).resolve().parents[1]
if str(COURSE) not in sys.path: sys.path.insert(0,str(COURSE))
import streamlit as st
from shared.streamlit_common import client_panel
from shared.demo_project import DOCS
from shared.rag import RAG
st.set_page_config(page_title="Module 7 · RAG Pipeline",layout="wide"); st.title("Module 7 · Building and Improving a RAG Pipeline")
client=client_panel(); size=st.slider("Chunk size (words)",10,150,40); overlap=st.slider("Overlap",0,min(30,size-1),10); k=st.slider("Top-k",1,5,3); q=st.text_input("Query","How should a checkout defect be handled?")
if st.button("Build embedding index and retrieve"):
    rag=RAG(client,DOCS,size,overlap); hits=rag.retrieve(q,k)
    st.write(f"Indexed {len(rag.rows)} chunks using {client.embedding_model}.")
    for h in hits: st.write(h["source"],f"{h['score']:.3f}"); st.code(h["text"])
    ans,_=rag.answer(q,k); st.markdown(ans)
