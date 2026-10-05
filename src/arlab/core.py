"""Core abstractions for deterministic, testable AI research pipelines."""

from __future__ import annotations

from dataclasses import dataclass, field
from time import perf_counter
from typing import Any, Callable, Iterable, Protocol
from uuid import uuid4


@dataclass(frozen=True)
class Evidence:
    """A traceable piece of evidence supporting a claim."""

    source: str
    content: str
    score: float = 1.0
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.source.strip():
            raise ValueError("Evidence source cannot be empty.")
        if not 0.0 <= self.score <= 1.0:
            raise ValueError("Evidence score must be between 0 and 1.")


@dataclass
class AgentContext:
    """Shared execution context passed between agents."""

    task: str
    inputs: dict[str, Any] = field(default_factory=dict)
    evidence: list[Evidence] = field(default_factory=list)
    memory: dict[str, Any] = field(default_factory=dict)
    trace_id: str = field(default_factory=lambda: uuid4().hex)


@dataclass
class AgentResult:
    """A normalized result returned by an agent."""

    agent: str
    output: Any
    confidence: float = 0.0
    evidence: list[Evidence] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)
    duration_ms: float = 0.0

    def __post_init__(self) -> None:
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("Confidence must be between 0 and 1.")


@dataclass
class VerificationResult:
    """Result of checking an agent output."""

    passed: bool
    score: float
    reasons: list[str] = field(default_factory=list)
    contradictions: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not 0.0 <= self.score <= 1.0:
            raise ValueError("Verification score must be between 0 and 1.")


@dataclass
class PipelineResult:
    """Complete, inspectable pipeline execution."""

    output: Any
    steps: list[AgentResult]
    verification: VerificationResult | None
    trace_id: str
    duration_ms: float


class Agent(Protocol):
    name: str

    def run(self, context: AgentContext) -> AgentResult:
        ...


class Pipeline:
    """Sequential orchestration with shared context and optional verification."""

    def __init__(self, agents: Iterable[Agent], verifier: Any | None = None) -> None:
        self.agents = list(agents)
        self.verifier = verifier

    def run(self, task: str, inputs: dict[str, Any] | None = None) -> PipelineResult:
        context = AgentContext(task=task, inputs=inputs or {})
        steps: list[AgentResult] = []
        started = perf_counter()

        for agent in self.agents:
            result = agent.run(context)
            steps.append(result)
            context.inputs[f"agent:{agent.name}"] = result.output
            context.evidence.extend(result.evidence)

        output = steps[-1].output if steps else None
        verification = None
        if self.verifier is not None:
            verification = self.verifier.verify(context, output)

        return PipelineResult(
            output=output,
            steps=steps,
            verification=verification,
            trace_id=context.trace_id,
            duration_ms=(perf_counter() - started) * 1000,
        )


def timed_call(fn: Callable[[], Any]) -> tuple[Any, float]:
    """Execute a callable and return its result plus elapsed milliseconds."""
    started = perf_counter()
    result = fn()
    return result, (perf_counter() - started) * 1000
