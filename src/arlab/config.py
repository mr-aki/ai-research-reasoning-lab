"""Configuration model kept dependency-free for portability."""

from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    environment: str = "development"
    log_level: str = "INFO"
    max_agents: int = 32
    verification_threshold: float = 0.5

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            environment=os.getenv("ARLAB_ENV", "development"),
            log_level=os.getenv("ARLAB_LOG_LEVEL", "INFO"),
            max_agents=int(os.getenv("ARLAB_MAX_AGENTS", "32")),
            verification_threshold=float(os.getenv("ARLAB_VERIFICATION_THRESHOLD", "0.5")),
        )
