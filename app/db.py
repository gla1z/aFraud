from databases import Database
from sqlalchemy import MetaData

DATABASE_URL = "postgresql+asyncpg://postgres:P@ssw0rd@localhost:5432/aFraud"

database = Database(DATABASE_URL)
metadata = MetaData()
