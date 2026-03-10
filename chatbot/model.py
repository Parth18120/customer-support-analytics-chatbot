from __future__ import annotations

import json
import random
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

from .preprocessing import preprocess


DATA_PATH = Path(__file__).resolve().parent.parent / "data" / "intents.json"


@dataclass
class PredictionResult:
    intent: str
    response: str
    confidence: float
    fallback: bool = False


class ChatbotModel:
    def __init__(self, confidence_threshold: float = 0.45) -> None:
        self.confidence_threshold = confidence_threshold
        self.intents = self._load_intents()
        self.responses_by_tag = {
            item["tag"]: item["responses"] for item in self.intents["intents"]
        }
        self.pipeline = self._train_model()

    def _load_intents(self) -> Dict[str, List[dict]]:
        with open(DATA_PATH, "r", encoding="utf-8") as file:
            return json.load(file)

    def _build_training_data(self) -> tuple[List[str], List[str]]:
        texts: List[str] = []
        labels: List[str] = []
        for intent in self.intents["intents"]:
            for pattern in intent["patterns"]:
                texts.append(pattern)
                labels.append(intent["tag"])
        return texts, labels

    def _train_model(self) -> Pipeline:
        texts, labels = self._build_training_data()
        pipeline = Pipeline(
            [
                ("vectorizer", CountVectorizer(analyzer=preprocess)),
                ("classifier", MultinomialNB()),
            ]
        )
        pipeline.fit(texts, labels)
        return pipeline

    def predict(self, message: str) -> PredictionResult:
        probabilities = self.pipeline.predict_proba([message])[0]
        classes = list(self.pipeline.classes_)
        best_index = int(probabilities.argmax())
        best_intent = classes[best_index]
        confidence = float(probabilities[best_index])

        if confidence < self.confidence_threshold:
            return PredictionResult(
                intent="fallback",
                response=(
                    "I’m not fully confident about that answer. "
                    "Please contact support@example.com for help."
                ),
                confidence=confidence,
                fallback=True,
            )

        response = random.choice(self.responses_by_tag[best_intent])
        return PredictionResult(
            intent=best_intent,
            response=response,
            confidence=confidence,
            fallback=False,
        )
