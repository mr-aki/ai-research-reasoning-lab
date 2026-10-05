# Roadmap

The roadmap is deliberately incremental: every layer must have working code, tests and measurable experiments before it is described as production-ready.

## Phase 1 — Research-grade foundation
- [x] Agent/context/result abstractions
- [x] Evidence and verification
- [x] Transparent retrieval baseline
- [x] Evaluation harness
- [x] Tool registry
- [x] Memory abstraction
- [x] Structured tracing
- [x] Unit tests and CI configuration

## Phase 2 — Grounded retrieval
- [x] Deterministic document chunking
- [x] Citation/provenance formatting
- [ ] Vector retrieval adapters
- [ ] Hybrid retrieval
- [ ] Reranking
- [ ] Retrieval evaluation suite
- [ ] Connector interfaces for web/search/database sources

## Phase 3 — Multi-agent reasoning
- [x] Model-provider interface
- [x] Independent agent execution
- [x] Baseline consensus aggregation
- [x] Deterministic routing baseline
- [ ] Role-specialized model-backed agents
- [ ] Parallel execution with budgets
- [ ] Critic/reviewer agents
- [ ] Debate and consensus protocols
- [ ] Conflict-aware synthesis
- [ ] Adaptive routing

## Phase 4 — Trust and evaluation
- [x] Evaluation harness
- [x] Calibration metric baseline
- [x] Explicit abstention policy
- [x] Conservative lexical contradiction baseline
- [ ] Benchmark registry
- [ ] Hallucination/grounding metrics
- [ ] Semantic contradiction detection
- [ ] Robustness/adversarial evaluation
- [ ] Regression dashboard

## Phase 5 — Tool-augmented intelligence
- [x] Explicit tool registry
- [ ] Permission scopes
- [ ] Sandboxed code execution
- [ ] Search/web connectors
- [ ] Database connectors
- [ ] Budgets and timeouts
- [ ] Audit trails
- [ ] Prompt-injection defenses

## Phase 6 — Model layer
- [x] Unified model interface
- [ ] Local model adapter
- [ ] Hosted model adapters
- [ ] Streaming
- [ ] Cost and latency accounting
- [ ] Model routing
- [ ] Retry/circuit-breaker policies

## Phase 7 — Research platform
- [ ] Experiment registry
- [ ] Dataset/version registry
- [ ] Run artifacts
- [ ] Reproducibility manifests
- [ ] Research reports
- [ ] Interactive evaluation dashboard
- [ ] Model/provider comparison

## Phase 8 — Advanced research
- [ ] Long-horizon planning
- [ ] Memory retrieval and consolidation
- [ ] Independent self-critique
- [ ] Tool planning
- [ ] Search over reasoning strategies
- [ ] Scaling experiments
- [ ] Reliability/cost frontier studies

## Non-negotiable standard

A feature is not considered complete because it exists in code. It is complete when its behavior is tested, its limitations are documented, and any performance or reliability claim is supported by a reproducible measurement.
