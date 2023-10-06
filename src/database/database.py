import sqlalchemy as db

from src.database.config import DB_URL
from sqlalchemy.orm import declarative_base


engine = db.create_engine(DB_URL)
Base = declarative_base()
