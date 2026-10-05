"""Structured tracing records for reproducible agent runs."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any


@dataclass
class TraceEvent:
    name: str
    event_type: str
    timestamp: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    payload: dict[str, Any] = field(default_factory=dict)


class Trace:
    def __init__(self) -> None:
        self.events: list[TraceEvent] = []

    def record(self, name: str, event_type: str, **payload: Any) -> TraceEvent:
        event = TraceEvent(name=name, event_type=event_type, payload=payload)
        self.events.append(event)
        return event

    def export(self) -> list[dict[str, Any]]:
        return [asdict(event) for event in self.events]
