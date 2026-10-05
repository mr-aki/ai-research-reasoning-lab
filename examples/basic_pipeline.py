"""Run the smallest end-to-end pipeline.

Usage:
    python examples/basic_pipeline.py
"""

from arlab.agents import EchoAgent, ResearchAgent
from arlab.core import Evidence, Pipeline
from arlab.verification import BasicVerifier

pipeline = Pipeline([EchoAgent(), ResearchAgent()], verifier=BasicVerifier())

result = pipeline.run(
    "What makes an AI answer trustworthy?",
    inputs={
        "seed_evidence": [
            Evidence(
                source="example",
                content="Trustworthy AI requires explicit evidence and evaluation.",
                score=0.9,
            )
        ]
    },
)

# The baseline pipeline intentionally keeps evidence explicit.
print(result.output)
print("verified:", result.verification.passed if result.verification else None)
