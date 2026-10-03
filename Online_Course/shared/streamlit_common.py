from __future__ import annotations
import streamlit as st
from .ollama_client import OllamaClient

def client_panel():
    with st.sidebar:
        st.header("Local AI")
        base=st.text_input("Ollama URL","http://localhost:11434")
        model=st.text_input("Chat model","qwen3:4b")
        emb=st.text_input("Embedding model","embeddinggemma")
    c=OllamaClient(base,model,emb)
    models=c.models()
    if models: st.sidebar.success("Ollama connected"); st.sidebar.caption("Installed: "+", ".join(models[:8]))
    else: st.sidebar.error("Ollama not reachable or no models installed.")
    return c
