"""Module 2 demo: next-token prediction and the effect of context.

This is a teaching simulation, not an implementation of a real LLM.
It uses small hand-written probability tables so the behavior is transparent.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Prediction:
    token: str
    probability: float


PREDICTIONS = {
    "mary had a little": [
        Prediction("lamb", 0.82),
        Prediction("dog", 0.08),
        Prediction("house", 0.05),
        Prediction("idea", 0.05),
    ],
    "for i in range(": [
        Prediction("10", 0.45),
        Prediction("len(items)", 0.35),
        Prediction("n", 0.15),
        Prediction("1", 0.05),
    ],
    "items = ['a', 'b', 'c']\nfor i in range(": [
        Prediction("len(items)", 0.78),
        Prediction("3", 0.12),
        Prediction("10", 0.06),
        Prediction("n", 0.04),
    ],
}


def predict_next(context: str) -> list[Prediction]:
    """Return the teaching distribution for an exact context."""
    key = context.strip().lower()
    if key not in PREDICTIONS:
        raise KeyError(f"No teaching distribution for: {context!r}")
    return PREDICTIONS[key]


def show(context: str) -> None:
    print(f"Context: {context!r}")
    for prediction in predict_next(context):
        print(f"  {prediction.token:<12} {prediction.probability:>6.0%}")
    print()


if __name__ == "__main__":
    show("Mary had a little")
    show("for i in range(")
    show("items = ['a', 'b', 'c']\nfor i in range(")
