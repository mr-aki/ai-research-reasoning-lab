"""Command-line entry point."""

from __future__ import annotations

import argparse
import json

from .agents import EchoAgent
from .core import Pipeline


def main() -> None:
    parser = argparse.ArgumentParser(description="AI Research & Reasoning Lab")
    parser.add_argument("task", nargs="?", default="Explain why reproducible evaluation matters.")
    args = parser.parse_args()

    result = Pipeline([EchoAgent()]).run(args.task)
    print(json.dumps({
        "trace_id": result.trace_id,
        "output": result.output,
        "duration_ms": round(result.duration_ms, 3),
    }, indent=2))
