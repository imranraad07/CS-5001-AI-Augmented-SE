# Module 7: Building a RAG Pipeline

An inspectable local baseline: **documents → chunks → vectors → cosine similarity → top-k retrieval**. The vectorizer is intentionally simple so students can see every step; production embedding models/vector stores are discussed in the lecture, not simulated here.

Run:
```bash
cd Online_Course/Module_07_RAG_Pipeline
python rag_pipeline.py
pytest -q
```

During recording, change chunk size, overlap, query, and `k` to demonstrate retrieval failure and improvement. Connect this to the lecture's chunking, embeddings, top-k, citation, and evaluation concepts.
