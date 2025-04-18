from typing import Dict

def apply_rules(tx: Dict) -> Dict:
    """
    Примитивный Rules Engine для оценки риска транзакции.
    Возвращает словарь с флагом риска и объяснением.
    """

    risk_score = 0
    reasons = []

    # Пример 1: Сумма больше 5000
    if tx["amount"] > 5000:
        risk_score += 40
        reasons.append("High amount")

    # Пример 2: Страна не из доверенного списка
    trusted_countries = {"RU", "BY", "KZ"}
    if tx["country"] not in trusted_countries:
        risk_score += 30
        reasons.append("Untrusted country")
    
    # Пример 3: Пустой merchant_id
    if not tx.get("merchant_id"):
        risk_score += 20
        reasons.append("Missing merchant ID")
    
    is_fraud = risk_score >= 50

    return {
        "risk_score": risk_score,
        "is_fraud": is_fraud,
        "reasons": reasons
    }