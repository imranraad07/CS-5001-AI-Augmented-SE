"""Module 7: inspectable baseline RAG pipeline using local TF/cosine-style vectors."""
from __future__ import annotations
from collections import Counter
from dataclasses import dataclass
from math import sqrt
import re

@dataclass(frozen=True)
class Chunk:
    source: str
    text: str

def tokenize(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower())

def chunk_document(source: str, text: str, size: int = 24, overlap: int = 4) -> list[Chunk]:
    if size <= 0 or overlap < 0 or overlap >= size:
        raise ValueError("require size > 0 and 0 <= overlap < size")
    words = text.split()
    step = size - overlap
    return [Chunk(source, " ".join(words[i:i+size])) for i in range(0, len(words), step) if words[i:i+size]]

def embed(text: str) -> Counter:
    return Counter(tokenize(text))

def cosine(a: Counter, b: Counter) -> float:
    common = set(a) & set(b)
    dot = sum(a[t] * b[t] for t in common)
    na = sqrt(sum(v*v for v in a.values()))
    nb = sqrt(sum(v*v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0

class Index:
    def __init__(self, chunks: list[Chunk]):
        self.rows = [(c, embed(c.text)) for c in chunks]

    def search(self, query: str, k: int = 3) -> list[tuple[float, Chunk]]:
        q = embed(query)
        ranked = sorted(((cosine(q, v), c) for c, v in self.rows), reverse=True, key=lambda x: x[0])
        return [(score, c) for score, c in ranked if score > 0][:k]

if __name__ == "__main__":
    docs = {
        "CONTRIBUTING.md": "Pull requests require unit tests, lint checks, and one approving review before merge.",
        "payments.md": "The payments client timeout is five seconds. Retry transient failures twice with exponential backoff.",
        "RUNBOOK.md": "If deployment health checks fail, roll back to the previous release and verify service health.",
    }
    chunks = [c for name, text in docs.items() for c in chunk_document(name, text, size=12, overlap=2)]
    index = Index(chunks)
    for score, chunk in index.search("What checks are required before merge?"):
        print(f"{score:.3f} {chunk.source}: {chunk.text}")
