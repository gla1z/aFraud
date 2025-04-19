from typing import Dict
from rules_loader import load_rules

rules = load_rules()

def apply_rules(tx: Dict) -> Dict:
    """
    Примитивный Rules Engine для оценки риска транзакции.
    Возвращает словарь с флагом риска и объяснением.
    """

    total_score = 0
    triggered = []

    for rule in sorted(rules, key=lambda r: r.priority):
        if not rule.enabled:
            continue

        try:
            if eval(rule.condition, {}, tx):
                triggered.append(rule.id)
                total_score += rule.risk_score
        except Exception as e:
            print(f"Rule {rule.id} failed: {e}")

    return {
        "risk_score": total_score,
        "is_fraud": total_score > 0,
        "reasons": triggered
    }