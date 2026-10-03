"""Module 6: tiny keyword RAG demo. Retrieval is real; generation is templated."""
from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Document:
    source: str
    text: str

DOCS = [
    Document("CONTRIBUTING.md", "Before merge, run unit tests and obtain one code review approval."),
    Document("RUNBOOK.md", "Rollback a failed deployment by restoring the previous release and verifying health checks."),
    Document("OWNERS.md", "The checkout team owns the /v2/checkout endpoint."),
]

def terms(text: str) -> set[str]:
    return set(re.findall(r"[a-z0-9]+", text.lower()))

def retrieve(query: str, k: int = 2) -> list[Document]:
    q = terms(query)
    ranked = sorted(DOCS, key=lambda d: len(q & terms(d.text)), reverse=True)
    return [d for d in ranked if q & terms(d.text)][:k]

def grounded_prompt(query: str, docs: list[Document]) -> str:
    sources = "\n".join(f"[S{i}] {d.source}: {d.text}" for i, d in enumerate(docs, 1))
    return f"""Answer using only SOURCES. If unsupported, say: I don't know.
Cite [S1], [S2], etc.

QUESTION:
{query}

SOURCES:
{sources or "(none retrieved)"}"""

if __name__ == "__main__":
    q = "What checks are required before merge?"
    hits = retrieve(q)
    print("Retrieved:", [d.source for d in hits])
    print(grounded_prompt(q, hits))
