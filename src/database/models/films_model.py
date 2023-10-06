from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.database.database import Base


class Film(Base):
    __tablename__ = 'Film'
    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(length=100), nullable=False)
    genre = Column(String(length=100), nullable=False)

    ratings = relationship("Rating", back_populates="film")
    comments = relationship("Comment", back_populates="film")

    def __repr__(self):
        return f'{self.title}'
