"""AI Research & Reasoning Lab public API."""

from .agents import EchoAgent, FunctionAgent, ResearchAgent
from .claims import Claim
from .core import (
    Agent,
    AgentContext,
    AgentResult,
    Evidence,
    Pipeline,
    PipelineResult,
    VerificationResult,
)
from .models import Model, ModelResponse
from .reasoning import ConsensusResult, MajorityConsensus, run_independent_agents
from .verification import BasicVerifier, VerificationPolicy

__version__ = "0.1.0"

__all__ = [
    "Agent",
    "AgentContext",
    "AgentResult",
    "Evidence",
    "Pipeline",
    "PipelineResult",
    "VerificationResult",
    "EchoAgent",
    "FunctionAgent",
    "ResearchAgent",
    "Claim",
    "Model",
    "ModelResponse",
    "ConsensusResult",
    "MajorityConsensus",
    "run_independent_agents",
    "BasicVerifier",
    "VerificationPolicy",
    "__version__",
]
