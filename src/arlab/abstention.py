"""Explicit abstention policy for uncertain or poorly grounded outputs."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class AbstentionPolicy:
    min_confidence: float = 0.5
    min_evidence: int = 1

    def should_abstain(self, *, confidence: float, evidence_count: int) -> bool:
        if not 0.0 <= confidence <= 1.0:
            raise ValueError("confidence must be between 0 and 1")
        return confidence < self.min_confidence or evidence_count < self.min_evidence
