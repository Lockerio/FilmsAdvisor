from sqlalchemy import Column, Integer, String, ForeignKey, Text
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


class Film(Base):
    __tablename__ = 'Film'
    id = Column(Integer(), primary_key=True, nullable=False, autoincrement=True)
    title = Column(String(length=100), nullable=False)
    genre = Column(String(length=100), nullable=False)

    ratings = relationship("Rating", back_populates="film")
    comments = relationship("Comment", back_populates="film")

    def __repr__(self):
        return f'{self.title}'


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
