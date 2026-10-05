# Architecture

## Design goals

1. Explicit evidence and provenance.
2. Composable, replaceable agents.
3. Inspectable execution with traces and intermediate results.
4. Reproducible evaluation.
5. Safe capability boundaries.

## Current pipeline

Task -> AgentContext -> Agents -> Shared Evidence/Memory -> Verifier -> PipelineResult

## Planned production layers

- Model adapters: local and hosted models behind one interface.
- Retrieval: lexical, vector, hybrid and reranking backends.
- Orchestration: routing, parallel branches, debate, critique and synthesis.
- Verification: source support, contradiction detection, calibration and abstention.
- Tool runtime: permissioned tools with budgets, timeouts and audit logs.
- Evaluation: benchmark registry, regression tracking and experiment comparison.
- Observability: structured traces, cost/latency accounting and failure analysis.
