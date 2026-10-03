from rag_demo import grounded_prompt, retrieve

def test_merge_query_retrieves_contributing():
    assert retrieve("What checks are required before merge?")[0].source == "CONTRIBUTING.md"

def test_prompt_requires_grounding():
    p = grounded_prompt("question", [])
    assert "using only SOURCES" in p
    assert "I don't know" in p
