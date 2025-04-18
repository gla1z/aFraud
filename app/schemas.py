from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class TransactionRequest(BaseModel):
    transaction_id: str
    user_id: str
    amount: float
    country: str
    timestamp: datetime
    merchant_id: Optional[str] = None

class TransactionResponse(BaseModel):
    risk_score: int
    ml_score: float
    rules_triggered: List[str]
    final_decision: bool
