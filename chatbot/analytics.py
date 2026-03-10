from __future__ import annotations

from pathlib import Path

import pandas as pd


LOG_PATH = Path(__file__).resolve().parent.parent / "data" / "chat_logs.csv"


def summarize_logs() -> dict:
    if not LOG_PATH.exists() or LOG_PATH.stat().st_size == 0:
        return {
            "total_conversations": 0,
            "fallback_rate": 0,
            "average_confidence": 0,
            "top_intents": {},
        }

    df = pd.read_csv(LOG_PATH)
    if df.empty:
        return {
            "total_conversations": 0,
            "fallback_rate": 0,
            "average_confidence": 0,
            "top_intents": {},
        }

    top_intents = (
        df.loc[df["predicted_intent"] != "fallback", "predicted_intent"]
        .value_counts()
        .head(5)
        .to_dict()
    )

    return {
        "total_conversations": int(len(df)),
        "fallback_rate": round(float(df["fallback"].mean()) * 100, 2),
        "average_confidence": round(float(df["confidence"].mean()), 4),
        "top_intents": top_intents,
    }


if __name__ == "__main__":
    summary = summarize_logs()
    print("Chatbot Analytics Summary")
    print("-" * 30)
    for key, value in summary.items():
        print(f"{key}: {value}")
