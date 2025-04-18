from rules import apply_rules
from ml_model import predict_fraud
from typing import Dict

RISK_THRESHOLD = 0.5

def analyze_transaction(transaction: Dict) -> Dict:
    rules_result = apply_rules(transaction)
    ml_score = predict_fraud(transaction)
    final_decision = bool(rules_result["is_fraud"] or ml_score >= RISK_THRESHOLD)

    return {
        "risk_score": int(rules_result["risk_score"]),
        "rules_triggered": rules_result["reasons"],
        "ml_score": float(round(ml_score, 4)),
        "final_decision": final_decision
    }
