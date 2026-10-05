"""Small end-to-end grounded pipeline example."""

from arlab.agents import ResearchAgent
from arlab.core import Evidence, Pipeline
from arlab.verification import BasicVerifier

pipeline = Pipeline([ResearchAgent()], verifier=BasicVerifier())

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

print("answer:", result.output)
print("verified:", result.verification.passed if result.verification else None)
print("trace:", result.trace_id)
