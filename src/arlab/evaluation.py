"""Evaluation primitives that produce reproducible, inspectable metrics."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, Any


@dataclass(frozen=True)
class Case:
    case_id: str
    input: Any
    expected: Any


@dataclass(frozen=True)
class CaseResult:
    case_id: str
    passed: bool
    score: float
    actual: Any
    expected: Any


@dataclass(frozen=True)
class EvaluationReport:
    total: int
    passed: int
    accuracy: float
    cases: tuple[CaseResult, ...]


def evaluate(
    cases: Iterable[Case],
    predict: Callable[[Any], Any],
    score_fn: Callable[[Any, Any], float] | None = None,
) -> EvaluationReport:
    cases = list(cases)
    if not cases:
        return EvaluationReport(total=0, passed=0, accuracy=0.0, cases=())

    scorer = score_fn or (lambda actual, expected: 1.0 if actual == expected else 0.0)
    results: list[CaseResult] = []

    for case in cases:
        actual = predict(case.input)
        score = max(0.0, min(1.0, float(scorer(actual, case.expected))))
        results.append(
            CaseResult(
                case_id=case.case_id,
                passed=score >= 1.0,
                score=score,
                actual=actual,
                expected=case.expected,
            )
        )

    passed = sum(result.passed for result in results)
    return EvaluationReport(
        total=len(results),
        passed=passed,
        accuracy=sum(r.score for r in results) / len(results),
        cases=tuple(results),
    )
