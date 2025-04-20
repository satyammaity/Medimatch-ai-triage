from transformers import pipeline
import torch

# Load the model (runs once)
classifier = pipeline(
    "text-classification",
    model="bhadresh-savani/distilbert-base-uncased-emotion",
    return_all_scores=True,
    device=0 if torch.cuda.is_available() else -1
)

# Map emotion labels to medical severity levels
SEVERITY_MAP = {
    "joy": "low",
    "love": "low",
    "neutral": "moderate",
    "surprise": "moderate",
    "sadness": "high",
    "disgust": "high",
    "anger": "critical",
    "fear": "critical"
}


def classify_severity(text):
    results = classifier(text)[0]
    top_result = max(results, key=lambda r: r['score'])
    emotion = top_result['label']
    confidence = top_result['score']

    severity = SEVERITY_MAP.get(emotion.lower(), "moderate")
    explanation = (
        f"The text expresses a strong sense of '{emotion}' "
        f"(confidence: {confidence:.2f}), "
        f"which maps to '{severity}' severity level."
    )

    return severity, explanation