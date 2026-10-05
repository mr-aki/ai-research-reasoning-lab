"""Confidence calibration metrics."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CalibrationReport:
    sample_count: int
    mean_confidence: float
    observed_accuracy: float
    mean_absolute_gap: float


def evaluate_calibration(confidences: list[float], outcomes: list[bool]) -> CalibrationReport:
    if len(confidences) != len(outcomes):
        raise ValueError("confidences and outcomes must have equal length")
    if not confidences:
        return CalibrationReport(0, 0.0, 0.0, 0.0)

    for confidence in confidences:
        if not 0.0 <= confidence <= 1.0:
            raise ValueError("confidence values must be between 0 and 1")

    mean_conf = sum(confidences) / len(confidences)
    accuracy = sum(outcomes) / len(outcomes)
    gap = sum(abs(c - float(o)) for c, o in zip(confidences, outcomes)) / len(outcomes)
    return CalibrationReport(len(outcomes), mean_conf, accuracy, gap)
