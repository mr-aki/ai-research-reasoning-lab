"""Dependency-free retrieval primitives for reproducible experiments."""

from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass

_TOKEN_RE = re.compile(r"[A-Za-z0-9_]+")


def tokenize(text: str) -> list[str]:
    return [token.lower() for token in _TOKEN_RE.findall(text)]


@dataclass(frozen=True)
class Document:
    document_id: str
    text: str
    metadata: dict[str, str] | None = None


class LexicalRetriever:
    """Small TF-IDF-like retriever used as a transparent baseline."""

    def __init__(self, documents: list[Document]) -> None:
        self.documents = documents
        self.term_counts = [Counter(tokenize(doc.text)) for doc in documents]
        self.doc_frequency: Counter[str] = Counter()
        for counts in self.term_counts:
            self.doc_frequency.update(counts.keys())

    def _idf(self, term: str) -> float:
        n = len(self.documents)
        df = self.doc_frequency.get(term, 0)
        return math.log((1 + n) / (1 + df)) + 1.0

    def _vector_score(self, query_terms: list[str], counts: Counter[str]) -> float:
        if not query_terms:
            return 0.0
        return sum(counts.get(term, 0) * self._idf(term) for term in query_terms)

    def search(self, query: str, top_k: int = 5) -> list[tuple[Document, float]]:
        if top_k <= 0:
            raise ValueError("top_k must be positive.")
        terms = tokenize(query)
        scored = [
            (doc, self._vector_score(terms, counts))
            for doc, counts in zip(self.documents, self.term_counts)
        ]
        return sorted(scored, key=lambda pair: pair[1], reverse=True)[:top_k]
