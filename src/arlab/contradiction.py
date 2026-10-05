"""Conservative lexical contradiction baseline.

This module deliberately does not claim semantic contradiction detection.
It identifies a small, interpretable class of conflicts for experimentation.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

_NEGATIONS = {"not", "no", "never", "without", "false"}
_WORDS = re.compile(r"[a-z0-9]+")


@dataclass(frozen=True)
class Contradiction:
    left: str
    right: str
    reason: str


def _tokens(text: str) -> set[str]:
    return set(_WORDS.findall(text.lower()))


def find_lexical_contradictions(statements: list[str]) -> list[Contradiction]:
    results: list[Contradiction] = []
    for i, left in enumerate(statements):
        left_tokens = _tokens(left)
        left_negated = bool(left_tokens & _NEGATIONS)
        for right in statements[i + 1:]:
            right_tokens = _tokens(right)
            right_negated = bool(right_tokens & _NEGATIONS)
            overlap = left_tokens & right_tokens - _NEGATIONS
            if overlap and left_negated != right_negated:
                results.append(Contradiction(
                    left=left,
                    right=right,
                    reason="High lexical overlap with opposite negation markers.",
                ))
    return results
