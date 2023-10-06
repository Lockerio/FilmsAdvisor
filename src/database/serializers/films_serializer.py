from sqlalchemy import func

from src.models import Film


class FilmSerializer:
    def __init__(self, session):
        self.session = session

    def get_one(self, film_id):
        return self.session.query(Film).get(film_id)

    def get_random_one_by_genre(self, genre):
        return self.session.query(Film).filter_by(genre=genre).order_by(func.random()).first()

    def get_all(self):
        return self.session.query(Film).all()

    def get_all_by_genre(self, genre):
        return self.session.query(Film).filter_by(genre=genre).all()

    def create(self, data):
        film = Film(**data)
        self.session.add(film)
        self.session.commit()
        return film

    def update(self, film):
        self.session.add(film)
        self.session.commit()
        return film

    def delete(self, film_id):
        film = self.get_one(film_id)
        self.session.delete(film)
        self.session.commit()
