import pickle
import os
from typing import Dict
import numpy as np

# Загружаем модель
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

def predict_fraud(transaction: Dict) -> float:
    # Простейший препроцессинг
    amount = transaction["amount"]
    country_risk = 1 if transaction["country"] not in ["RU", "BY", "KZ"] else 0
    missing_merchant = 1 if not transaction.get("merchant_id") else 0

    features = np.array([[amount, missing_merchant, country_risk]])
    prob = model.predict_proba(features)[0][1]
    return round(prob, 4)