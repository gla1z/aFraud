from sqlalchemy import Table, Column, String, Float, Boolean, Integer, JSON, DateTime
from datetime import datetime
from db import metadata

incidents = Table(
    "incidents",
    metadata,
    Column("transaction_id", String, primary_key=True),
    Column("user_id", String),
    Column("amount", Float),
    Column("country", String),
    Column("merchant_id", String, nullable=True),
    Column("timestamp", DateTime),
    Column("risk_score", Integer),
    Column("ml_score", Float),
    Column("rules_triggered", JSON),
    Column("final_decision", Boolean),
    Column("created_at", DateTime, default=datetime.utcnow),
)
