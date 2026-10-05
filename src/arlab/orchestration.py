"""Orchestration helpers for multi-agent workflows."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .core import Agent, AgentContext, AgentResult


@dataclass(frozen=True)
class OrchestrationDecision:
    selected_agent: str
    reason: str


class Router:
    """Deterministic router baseline.

    Later phases can replace this policy with learned routing while keeping
    the same interface and evaluation harness.
    """

    def __init__(self, agents: list[Agent]) -> None:
        if not agents:
            raise ValueError("Router requires at least one agent.")
        self.agents = agents

    def choose(self, context: AgentContext) -> OrchestrationDecision:
        return OrchestrationDecision(
            selected_agent=self.agents[0].name,
            reason="Baseline deterministic routing selected the first available agent.",
        )

    def run(self, context: AgentContext) -> AgentResult:
        decision = self.choose(context)
        agent = next(a for a in self.agents if a.name == decision.selected_agent)
        return agent.run(context)
