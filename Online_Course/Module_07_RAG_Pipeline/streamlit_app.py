import streamlit as st
st.set_page_config(page_title="Module 7 · RAG Pipeline",layout="wide"); st.title("Module 7 · Building and Improving a RAG Pipeline")
st.warning("Teaching implementation: lexical retrieval exposes mechanics; it is not a production embedding model.")
text=st.text_area("Document","Before merge run unit tests and lint checks. Checkout incidents should be reproduced before deployment. Changes require review."); size=st.slider("Chunk size",3,12,7); overlap=st.slider("Overlap",0,size-1,2)
w=text.split(); chunks=[]; i=0
while i<len(w):
    chunks.append(" ".join(w[i:i+size]))
    if i+size>=len(w): break
    i+=size-overlap
for j,c in enumerate(chunks): st.code(f"Chunk {j+1}: {c}")
q=st.text_input("Query","What happens before merge?"); score=lambda d:len(set(q.lower().split())&set(d.lower().split())); ranked=sorted(chunks,key=score,reverse=True); st.success("Top retrieved chunk: "+(ranked[0] if ranked else "None"))
