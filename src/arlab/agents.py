"""Reference agents used by the lab and its examples."""

from __future__ import annotations

from typing import Any, Callable

from .core import AgentContext, AgentResult, Evidence, timed_call


class EchoAgent:
    """A deterministic baseline agent for pipeline testing."""

    name = "echo"

    def run(self, context: AgentContext) -> AgentResult:
        output = context.task
        return AgentResult(agent=self.name, output=output, confidence=1.0)


class FunctionAgent:
    """Adapter that turns a normal Python function into an agent."""

    def __init__(self, name: str, function: Callable[[AgentContext], Any]) -> None:
        self.name = name
        self.function = function

    def run(self, context: AgentContext) -> AgentResult:
        output, duration = timed_call(lambda: self.function(context))
        return AgentResult(
            agent=self.name,
            output=output,
            confidence=0.5,
            duration_ms=duration,
        )


class ResearchAgent:
    """Simple evidence-aware synthesis agent.

    This baseline intentionally does not pretend to browse the internet.
    Production connectors can provide Evidence objects through AgentContext.
    """

    name = "researcher"

    def run(self, context: AgentContext) -> AgentResult:
        evidence = list(context.evidence)
        if not evidence:
            output = {
                "answer": "No external evidence was supplied.",
                "status": "ungrounded",
            }
            return AgentResult(
                agent=self.name,
                output=output,
                confidence=0.1,
                metadata={"evidence_count": 0},
            )

        snippets = [item.content.strip() for item in evidence if item.content.strip()]
        output = {
            "answer": "\n".join(snippets),
            "status": "grounded",
            "evidence_count": len(snippets),
        }
        confidence = min(0.95, 0.35 + 0.1 * len(snippets))
        return AgentResult(
            agent=self.name,
            output=output,
            confidence=confidence,
            evidence=evidence,
            metadata={"evidence_count": len(snippets)},
        )
