"""Ollama-embedding RAG over local project artifacts."""
from __future__ import annotations
import math
from pathlib import Path

def cosine(a,b):
    dot=sum(x*y for x,y in zip(a,b)); na=math.sqrt(sum(x*x for x in a)); nb=math.sqrt(sum(y*y for y in b))
    return dot/(na*nb) if na and nb else 0.0

def chunk_text(text,size=120,overlap=20):
    words=text.split(); out=[]; i=0
    while i<len(words):
        out.append(" ".join(words[i:i+size]))
        if i+size>=len(words): break
        i+=max(1,size-overlap)
    return out

class RAG:
    def __init__(self,client,documents,chunk_size=120,overlap=20):
        self.client=client; self.rows=[]
        for source,text in documents.items():
            for i,chunk in enumerate(chunk_text(text,chunk_size,overlap)): self.rows.append({"source":source,"chunk":i,"text":chunk})
        vectors=client.embed([r["text"] for r in self.rows])
        for r,v in zip(self.rows,vectors): r["vector"]=v
    def retrieve(self,query,k=3):
        q=self.client.embed(query)[0]
        ranked=sorted(self.rows,key=lambda r:cosine(q,r["vector"]),reverse=True)
        return [{**r,"score":cosine(q,r["vector"])} for r in ranked[:k]]
    def answer(self,query,k=3):
        hits=self.retrieve(query,k); context="\n".join(f"[S{i}] {h['source']}: {h['text']}" for i,h in enumerate(hits,1))
        prompt=f"""Answer only from SOURCES. If the sources do not support the answer, say I don't know.
Cite source IDs such as [S1].

QUESTION: {query}

SOURCES:
{context}"""
        return self.client.generate(prompt),hits
