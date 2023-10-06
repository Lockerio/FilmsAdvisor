from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from src.database.database import Base


class Rating(Base):
    __tablename__ = 'Rating'
    user_id = Column(Integer(), ForeignKey('User.id'), primary_key=True)
    film_id = Column(Integer(), ForeignKey('Film.id'), primary_key=True)
    rating = Column(Integer(), nullable=False)

    user = relationship("User", back_populates="ratings")
    film = relationship("Film", back_populates="ratings")

    def __repr__(self):
        return f"{self.user} - {self.film} = {self.rating}"
