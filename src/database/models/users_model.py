from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship

from src.database.database import Base


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    first_name = Column(String(length=100), nullable=False)
    last_name = Column(String(length=100), nullable=False)
    email = Column(String(length=100), nullable=False)
    hashed_password = Column(Text(), nullable=False)

    ratings = relationship("Rating", back_populates="user")
    comments = relationship("Comment", back_populates="user")

    def __repr__(self):
        return f'{self.first_name} {self.last_name}'
