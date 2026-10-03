from rag_pipeline import Index, chunk_document

def test_chunking_has_overlap():
    chunks = chunk_document("x", "one two three four five six seven", size=4, overlap=1)
    assert chunks[0].text.split()[-1] == chunks[1].text.split()[0]

def test_retrieval_finds_relevant_chunk():
    chunks = chunk_document("policy", "Pull requests require unit tests before merge.", size=20, overlap=2)
    assert Index(chunks).search("tests merge", 1)[0][1].source == "policy"
