"""Transparent multi-agent reasoning primitives.

These are intentionally model-agnostic. They provide orchestration structure;
they do not pretend that a heuristic consensus score is equivalent to truth.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Iterable

from .core import Agent, AgentContext, AgentResult


@dataclass(frozen=True)
class ConsensusResult:
    selected_output: Any
    agreement: float
    candidates: tuple[AgentResult, ...]


class MajorityConsensus:
    """Select the most repeated normalized output.

    This is useful as a baseline for experiments comparing aggregation
    strategies. It is not a truth oracle.
    """

    @staticmethod
    def _key(value: Any) -> str:
        return repr(value).strip().lower()

    def combine(self, results: Iterable[AgentResult]) -> ConsensusResult:
        candidates = tuple(results)
        if not candidates:
            raise ValueError("At least one result is required.")

        counts: dict[str, int] = {}
        for result in candidates:
            key = self._key(result.output)
            counts[key] = counts.get(key, 0) + 1

        best_key, best_count = max(counts.items(), key=lambda item: item[1])
        selected = next(result.output for result in candidates if self._key(result.output) == best_key)
        return ConsensusResult(
            selected_output=selected,
            agreement=best_count / len(candidates),
            candidates=candidates,
        )


def run_independent_agents(agents: list[Agent], context: AgentContext) -> list[AgentResult]:
    """Run agents independently over the same context.

    Shared mutable state should be avoided by agents when independence is
    required for an experiment.
    """
    return [agent.run(context) for agent in agents]
