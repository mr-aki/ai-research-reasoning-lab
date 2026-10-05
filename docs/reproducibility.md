# Reproducibility

A research run should be reproducible enough for another engineer to understand exactly what happened.

Record:

- Git commit SHA
- Python version
- OS/hardware when material
- dependency lock/version information
- model/provider/version
- prompt/template version where applicable
- dataset identifier/version
- random seed
- configuration
- evaluation command
- raw result artifact location
- timestamp

If a result depends on an external API whose behavior can change, record the provider/model/version and treat the result as time-bound.
