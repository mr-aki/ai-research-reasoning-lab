"""Minimal explicit memory abstractions; persistence is intentionally pluggable."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class MemoryStore:
    """In-process memory with explicit writes and deterministic reads."""

    values: dict[str, Any] = field(default_factory=dict)

    def put(self, key: str, value: Any) -> None:
        if not key.strip():
            raise ValueError("Memory key cannot be empty.")
        self.values[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        return self.values.get(key, default)

    def delete(self, key: str) -> bool:
        return self.values.pop(key, None) is not None

    def snapshot(self) -> dict[str, Any]:
        return dict(self.values)
