from arlab.agents import ResearchAgent
from arlab.core import Evidence, Pipeline
from arlab.verification import BasicVerifier, VerificationPolicy


def test_grounded_pipeline_can_pass() -> None:
    result = Pipeline([ResearchAgent()], verifier=BasicVerifier()).run(
        "question",
        {"seed_evidence": [Evidence("source", "supported fact", 0.9)]},
    )
    assert result.verification is not None
    assert result.verification.passed


def test_threshold_can_force_abstention() -> None:
    verifier = BasicVerifier(VerificationPolicy(min_evidence=2))
    result = Pipeline([ResearchAgent()], verifier=verifier).run(
        "question",
        {"seed_evidence": [Evidence("source", "one fact", 0.9)]},
    )
    assert result.verification is not None
    assert not result.verification.passed
