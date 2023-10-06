from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from src.database.database import Base


class Comment(Base):
    __tablename__ = 'Comment'
    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    user_id = Column(Integer(), ForeignKey('User.id'))
    film_id = Column(Integer(), ForeignKey('Film.id'))
    text = Column(Text())

    user = relationship("User", back_populates="comments")
    film = relationship("Film", back_populates="comments")

    def __repr__(self):
        return f"{self.user} - {self.film} = {self.text}"
