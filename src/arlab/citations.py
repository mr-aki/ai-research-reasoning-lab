"""Citation helpers that preserve evidence provenance."""

from __future__ import annotations

from dataclasses import dataclass

from .core import Evidence


@dataclass(frozen=True)
class Citation:
    source: str
    label: str
    excerpt: str


def citations_from_evidence(evidence: list[Evidence]) -> list[Citation]:
    return [
        Citation(
            source=item.source,
            label=f"[{index}]",
            excerpt=item.content.strip(),
        )
        for index, item in enumerate(evidence, start=1)
        if item.content.strip()
    ]


def format_citations(evidence: list[Evidence]) -> str:
    return "\n".join(
        f"{citation.label} {citation.source}: {citation.excerpt}"
        for citation in citations_from_evidence(evidence)
    )
