from __future__ import annotations

import re
from functools import lru_cache
from typing import List

from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


@lru_cache(maxsize=1)
def _stopwords() -> set[str]:
    return set(ENGLISH_STOP_WORDS)


def simple_lemmatize(token: str) -> str:
    # Lightweight rule-based normalization to avoid external downloads.
    if token.endswith("ies") and len(token) > 4:
        return token[:-3] + "y"
    if token.endswith("ing") and len(token) > 5:
        return token[:-3]
    if token.endswith("ed") and len(token) > 4:
        return token[:-2]
    if token.endswith("s") and len(token) > 3 and not token.endswith("ss"):
        return token[:-1]
    return token


def preprocess(text: str) -> List[str]:
    tokens = re.findall(r"[a-zA-Z]+", text.lower())
    return [
        simple_lemmatize(token)
        for token in tokens
        if token not in _stopwords()
    ]
