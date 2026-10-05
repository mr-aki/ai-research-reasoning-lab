from arlab.agents import EchoAgent
from arlab.core import Evidence, Pipeline
from arlab.verification import BasicVerifier


def test_pipeline_runs_and_returns_trace() -> None:
    result = Pipeline([EchoAgent()]).run("hello")
    assert result.output == "hello"
    assert result.trace_id
    assert len(result.steps) == 1


def test_evidence_validation() -> None:
    evidence = Evidence(source="unit-test", content="grounded", score=0.9)
    assert evidence.score == 0.9


def test_verifier_requires_evidence() -> None:
    result = Pipeline([EchoAgent()], verifier=BasicVerifier()).run("hello")
    assert result.verification is not None
    assert result.verification.passed is False
