import pickle
import os

from src.preprocess import clean_text
from src.patterns import detect_patterns

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "models", "model.pkl")
vectorizer_path = os.path.join(BASE_DIR, "models", "vectorizer.pkl")

model = pickle.load(open(model_path, "rb"))
vectorizer = pickle.load(open(vectorizer_path, "rb"))

def predict_text(text):
    clean = clean_text(text)
    vec = vectorizer.transform([clean])

    pred = model.predict(vec)[0]
    prob = model.predict_proba(vec)[0][1]

    return {
        "prediction": "fraud" if pred==1 else "safe",
        "confidence": float(prob),
        "patterns": detect_patterns(text)
    }