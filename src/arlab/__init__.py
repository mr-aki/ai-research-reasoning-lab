"""AI Research & Reasoning Lab public API."""

from .core import (
    Agent,
    AgentContext,
    AgentResult,
    Evidence,
    Pipeline,
    PipelineResult,
    VerificationResult,
)
from .agents import EchoAgent, FunctionAgent, ResearchAgent
from .verification import BasicVerifier, VerificationPolicy

__version__ = "0.1.0"

__all__ = [
    "Agent", "AgentContext", "AgentResult", "Evidence", "Pipeline",
    "PipelineResult", "VerificationResult", "EchoAgent", "FunctionAgent",
    "ResearchAgent", "BasicVerifier", "VerificationPolicy", "__version__",
]
