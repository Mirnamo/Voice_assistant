from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    ambient_duration: float = 1.0
    listen_timeout: float = 5.0
    phrase_time_limit: float = 10.0
    dynamic_energy_threshold: bool = True
    speech_rate: int = 165
    log_level: str = "INFO"

    @classmethod
    def from_env(cls) -> "Settings":
        return cls(
            ambient_duration=float(os.getenv("MYA_AMBIENT_DURATION", "1.0")),
            listen_timeout=float(os.getenv("MYA_LISTEN_TIMEOUT", "5.0")),
            phrase_time_limit=float(os.getenv("MYA_PHRASE_TIME_LIMIT", "10.0")),
            dynamic_energy_threshold=os.getenv("MYA_DYNAMIC_THRESHOLD", "true").lower() == "true",
            speech_rate=int(os.getenv("MYA_SPEECH_RATE", "165")),
            log_level=os.getenv("MYA_LOG_LEVEL", "INFO").upper(),
        )
