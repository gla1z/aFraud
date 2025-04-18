from db import database
from models import incidents
from datetime import datetime

async def save_incident(data: dict):
    if "created_at" not in data:
        data["created_at"] = datetime.utcnow()

    query = incidents.insert().values(**data)
    await database.execute(query)
