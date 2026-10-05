from arlab.chunking import chunk_text


def test_chunking_covers_document() -> None:
    chunks = chunk_text("doc", "abcdefghij", size=6, overlap=2)
    assert chunks[0].text == "abcdef"
    assert chunks[-1].end == 10
