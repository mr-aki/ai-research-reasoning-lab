# Evaluation

Evaluation is the mechanism that turns engineering claims into evidence.

## Minimum report

Every serious experiment should record:

- experiment ID
- question and hypothesis
- baseline
- intervention
- dataset/evaluation cases
- model/provider and version
- configuration
- random seed when relevant
- hardware/runtime
- latency
- cost when applicable
- primary metric
- secondary metrics
- failures
- confidence/uncertainty treatment
- limitations

## Recommended metrics

Depending on the task:

- exact match / task accuracy
- evidence recall and precision
- citation support rate
- contradiction rate
- abstention quality
- calibration error
- latency distribution (p50/p95/p99)
- token and monetary cost
- tool success rate
- regression rate

No metric is meaningful without its task definition and baseline.
