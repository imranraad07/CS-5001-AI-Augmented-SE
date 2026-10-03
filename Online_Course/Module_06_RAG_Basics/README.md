# Module 6: RAG, Giving AI Project Knowledge

This dependency-free demo implements **retrieval + grounded prompt construction**. Generation is intentionally left to the instructor's LLM interface.

Run:
```bash
cd Online_Course/Module_06_RAG_Basics
python rag_demo.py
pytest -q
```

Record: ask a repo-specific question without sources, run retrieval, display the retrieved source, then send the grounded prompt to an LLM. Emphasize citations and `I don't know` for unsupported questions.
