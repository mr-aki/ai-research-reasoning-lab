"""Claim-level structures for future citation and contradiction systems."""

from __future__ import annotations

from dataclasses import dataclass, field
from .core import Evidence


@dataclass(frozen=True)
class Claim:
    text: str
    evidence: tuple[Evidence, ...] = ()
    confidence: float = 0.0
    metadata: dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.text.strip():
            raise ValueError("Claim text cannot be empty.")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("Claim confidence must be between 0 and 1.")
