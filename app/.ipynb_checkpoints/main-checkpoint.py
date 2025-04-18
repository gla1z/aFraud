from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from rules import apply_rules # Импорт правил

app = FastAPI(title="aFraud - Antifraud API", version="0.1")

# Модель входных данных
class TransactionRequest(BaseModel):
    transaction_id: str
    user_id: str
    amount: float
    country: str
    timestamp: datetime
    merchant_id: Optional[str] = None


# Простой тестовый эндпоинт
@app.post("/check_transaction")
def check_transaction(tx: TransactionRequest):
    tx_dict = tx.dict()
    risk_result = apply_rules(tx_dict)

    return {
        "transaction_id": tx.transaction_id,
        "user_id": tx.user_id,
        "amount": tx.amount,
        "country": tx.country,
        "risk_score": risk_result["risk_score"],
        "is_fraud": risk_result["is_fraud"],
        "reasons": risk_result["reasons"]
    }