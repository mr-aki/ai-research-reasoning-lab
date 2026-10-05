"""Reference agents used by the lab and its examples."""

from __future__ import annotations

from typing import Any, Callable

from .core import AgentContext, AgentResult, Evidence, timed_call


class EchoAgent:
    """A deterministic baseline agent for pipeline testing."""

    name = "echo"

    def run(self, context: AgentContext) -> AgentResult:
        return AgentResult(agent=self.name, output=context.task, confidence=1.0)


class FunctionAgent:
    """Adapter that turns a Python function into an agent."""

    def __init__(self, name: str, function: Callable[[AgentContext], Any]) -> None:
        self.name = name
        self.function = function

    def run(self, context: AgentContext) -> AgentResult:
        output, duration = timed_call(lambda: self.function(context))
        return AgentResult(
            agent=self.name, output=output, confidence=0.5, duration_ms=duration
        )


class ResearchAgent:
    """Evidence-aware synthesis baseline.

    The agent never claims to browse. Evidence must be supplied explicitly
    by a connector, retriever, or experiment.
    """

    name = "researcher"

    def run(self, context: AgentContext) -> AgentResult:
        seeded = context.inputs.get("seed_evidence", [])
        if seeded:
            for item in seeded:
                if isinstance(item, Evidence):
                    context.evidence.append(item)

        evidence = list(context.evidence)
        if not evidence:
            return AgentResult(
                agent=self.name,
                output={"answer": "No external evidence was supplied.", "status": "ungrounded"},
                confidence=0.1,
                metadata={"evidence_count": 0},
            )

        snippets = [item.content.strip() for item in evidence if item.content.strip()]
        return AgentResult(
            agent=self.name,
            output={
                "answer": "\n".join(snippets),
                "status": "grounded",
                "evidence_count": len(snippets),
            },
            confidence=min(0.95, 0.35 + 0.1 * len(snippets)),
            evidence=evidence,
            metadata={"evidence_count": len(snippets)},
        )
