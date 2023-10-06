from src.models import Rating


class RatingSerializer:
    def __init__(self, session):
        self.session = session

    def get_one(self, film_id, user_id):
        return self.session.query(Rating).filter_by(film_id=film_id).get(user_id)

    def get_all(self):
        return self.session.query(Rating).all()

    def create(self, data):
        rating = Rating(**data)
        self.session.add(rating)
        self.session.commit()
        return rating

    def update(self, rating):
        self.session.add(rating)
        self.session.commit()
        return rating

    def delete(self, film_id, user_id):
        rating = self.get_one(film_id, user_id)
        self.session.delete(rating)
        self.session.commit()
