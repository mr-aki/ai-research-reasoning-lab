"""Deterministic document chunking for retrieval experiments."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Chunk:
    chunk_id: str
    document_id: str
    text: str
    start: int
    end: int


def chunk_text(document_id: str, text: str, *, size: int = 800, overlap: int = 120) -> list[Chunk]:
    if size <= 0:
        raise ValueError("size must be positive")
    if overlap < 0 or overlap >= size:
        raise ValueError("overlap must be >= 0 and < size")

    chunks: list[Chunk] = []
    start = 0
    index = 0
    while start < len(text):
        end = min(len(text), start + size)
        chunks.append(Chunk(f"{document_id}:{index}", document_id, text[start:end], start, end))
        if end == len(text):
            break
        start = end - overlap
        index += 1
    return chunks
