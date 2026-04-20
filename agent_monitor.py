from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


class Monitor:
    def __init__(self, agent_name: str, log_dir: str | None = None):
        self.agent_name = agent_name
        self.log_dir = Path(log_dir or "logs")
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self.metrics = {
            "token_usage": {
                "total_tokens": 0,
                "total_cost": 0.0,
                "calls": 0,
            },
            "latency": {
                "count": 0,
                "total_seconds": 0.0,
                "avg_seconds": 0.0,
                "max_seconds": 0.0,
            },
        }

    @property
    def events_path(self) -> Path:
        return self.log_dir / f"{self.agent_name}.events.jsonl"

    def track_token_usage(self, tokens: int, cost: float):
        usage = self.metrics["token_usage"]
        usage["total_tokens"] += int(tokens)
        usage["total_cost"] += float(cost)
        usage["calls"] += 1
        return dict(usage)

    def track_latency(self, seconds: float):
        latency = self.metrics["latency"]
        latency["count"] += 1
        latency["total_seconds"] += float(seconds)
        latency["avg_seconds"] = latency["total_seconds"] / latency["count"]
        latency["max_seconds"] = max(latency["max_seconds"], float(seconds))
        return dict(latency)

    def log(self, level: str, message: str, extra: dict[str, Any] | None = None):
        event = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "agent_name": self.agent_name,
            "level": level,
            "message": message,
        }
        if extra:
            event.update(extra)
        with self.events_path.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(event, ensure_ascii=False) + "\n")
        return event

    def snapshot(self) -> dict[str, Any]:
        return {
            "agent_name": self.agent_name,
            "token_usage": {
                **self.metrics["token_usage"],
                "total_cost": round(self.metrics["token_usage"]["total_cost"], 10),
            },
            "latency": {
                **self.metrics["latency"],
                "avg_seconds": round(self.metrics["latency"]["avg_seconds"], 10),
                "max_seconds": round(self.metrics["latency"]["max_seconds"], 10),
            },
        }
