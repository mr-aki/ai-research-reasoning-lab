"""Verification policies for grounded and internally consistent outputs."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .core import AgentContext, Evidence, VerificationResult


@dataclass(frozen=True)
class VerificationPolicy:
    min_evidence: int = 1
    min_score: float = 0.5
    require_grounding: bool = True


class BasicVerifier:
    """Conservative verifier for the first research pipeline.

    It checks structural grounding and evidence quality. It does not claim
    semantic truth beyond what the supplied evidence supports.
    """

    def __init__(self, policy: VerificationPolicy | None = None) -> None:
        self.policy = policy or VerificationPolicy()

    def verify(self, context: AgentContext, output: Any) -> VerificationResult:
        reasons: list[str] = []
        contradictions: list[str] = []
        evidence: list[Evidence] = context.evidence

        if self.policy.require_grounding and len(evidence) < self.policy.min_evidence:
            reasons.append("Insufficient evidence for a grounded answer.")

        if output is None:
            reasons.append("Pipeline produced no output.")

        scores = [item.score for item in evidence]
        evidence_score = sum(scores) / len(scores) if scores else 0.0
        score = evidence_score

        if evidence_score < self.policy.min_score:
            reasons.append("Average evidence score is below the verification threshold.")

        passed = not reasons
        if passed:
            reasons.append("Structural grounding checks passed.")

        return VerificationResult(
            passed=passed,
            score=score,
            reasons=reasons,
            contradictions=contradictions,
        )
