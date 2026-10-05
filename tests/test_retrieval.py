from arlab.retrieval import Document, LexicalRetriever


def test_retriever_ranks_relevant_document_first() -> None:
    retriever = LexicalRetriever([
        Document("a", "cats are mammals"),
        Document("b", "quantum computing uses qubits"),
        Document("c", "cats hunt mice"),
    ])
    results = retriever.search("cats mammals", top_k=2)
    assert results[0][0].document_id == "a"


def test_retriever_rejects_invalid_top_k() -> None:
    retriever = LexicalRetriever([Document("a", "hello")])
    try:
        retriever.search("hello", top_k=0)
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError")
