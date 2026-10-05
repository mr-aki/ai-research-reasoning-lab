# Security Model

Security is part of the architecture.

Current baseline:

- No arbitrary shell execution.
- No implicit network access.
- Explicit tool registration.
- Input validation at public boundaries.
- No secrets committed to the repository.
- Environment configuration separated from source code.

Planned:

- Tool permission scopes.
- Per-run budgets and timeouts.
- Sandboxed execution.
- Prompt-injection defenses for retrieved content.
- Secret redaction in traces.
- Audit logs.
- Dependency and supply-chain scanning.
