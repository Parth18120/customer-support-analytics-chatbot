from __future__ import annotations

import csv
from datetime import datetime
from pathlib import Path

from .model import PredictionResult


LOG_PATH = Path(__file__).resolve().parent.parent / "data" / "chat_logs.csv"


def ensure_log_file() -> None:
    if not LOG_PATH.exists() or LOG_PATH.stat().st_size == 0:
        with open(LOG_PATH, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow([
                "timestamp",
                "user_message",
                "predicted_intent",
                "confidence",
                "fallback",
                "bot_response",
            ])


def log_interaction(user_message: str, result: PredictionResult) -> None:
    ensure_log_file()
    with open(LOG_PATH, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                datetime.utcnow().isoformat(),
                user_message,
                result.intent,
                round(result.confidence, 4),
                result.fallback,
                result.response,
            ]
        )
