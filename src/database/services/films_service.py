from src.serializers.films_serializer import FilmSerializer


class FilmService:
    def __init__(self, serializer: FilmSerializer):
        self.serializer = serializer

    def get_one(self, film_id):
        return self.serializer.get_one(film_id)

    def get_random_one_by_genre(self, genre):
        return self.serializer.get_random_one_by_genre(genre)

    def get_all(self):
        return self.serializer.get_all()

    def get_all_by_genre(self, genre):
        return self.serializer.get_all_by_genre(genre)

    def update(self, data):
        return self.serializer.update(data)

    def create(self, data):
        return self.serializer.create(data)

    def delete(self, film_id):
        self.serializer.delete(film_id)
