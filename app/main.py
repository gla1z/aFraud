from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

from risk_detector import analyze_transaction
from persistence import save_incident
from db import database
from schemas import TransactionRequest, TransactionResponse

app = FastAPI(title="aFraud - Antifraud API", version="0.1")


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.post("/check_transaction", response_model=TransactionResponse)
async def check_transaction(tx: TransactionRequest):
    tx_dict = tx.dict()
    analysis = analyze_transaction(tx_dict)

    incident_data = {
        **tx_dict,
        **analysis
    }
    await save_incident(incident_data)

    return TransactionResponse(**analysis)