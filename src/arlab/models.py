"""Model-provider abstraction.

The lab never couples research code directly to a vendor SDK. Providers
implement this small interface and expose their model/version metadata.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Iterator


@dataclass(frozen=True)
class ModelResponse:
    text: str
    model: str
    usage: dict[str, int] | None = None
    metadata: dict[str, str] | None = None


class Model(Protocol):
    name: str

    def generate(self, prompt: str, *, temperature: float = 0.0) -> ModelResponse:
        ...


class StreamingModel(Model, Protocol):
    def stream(self, prompt: str, *, temperature: float = 0.0) -> Iterator[str]:
        ...
