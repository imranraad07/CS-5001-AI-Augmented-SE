"""Teaching simulation of next-token prediction. This is not a real LLM."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Prediction:
    token: str
    probability: float

PREDICTIONS = {
    "mary had a little": [Prediction("lamb", .82), Prediction("dog", .08), Prediction("house", .05), Prediction("idea", .05)],
    "for i in range(": [Prediction("10", .45), Prediction("len(items)", .35), Prediction("n", .15), Prediction("1", .05)],
    "items = ['a', 'b', 'c']\nfor i in range(": [Prediction("len(items)", .78), Prediction("3", .12), Prediction("10", .06), Prediction("n", .04)],
}

def predict_next(context: str) -> list[Prediction]:
    key = context.strip().lower()
    if key not in PREDICTIONS:
        raise KeyError(f"No teaching distribution for {context!r}")
    return PREDICTIONS[key]

def show(context: str) -> None:
    print(f"Context: {context!r}")
    for p in predict_next(context):
        print(f"  {p.token:<12} {p.probability:>6.0%}")
    print()

if __name__ == "__main__":
    show("Mary had a little")
    show("for i in range(")
    show("items = ['a', 'b', 'c']\nfor i in range(")
