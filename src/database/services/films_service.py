from src.database.serializers.films_serializer import FilmSerializer
from src.database.utils.formatter import Formatter
from src.database.utils.validator import Validator


class FilmService:
    def __init__(self, serializer: FilmSerializer):
        self.serializer = serializer

    def get_one(self, film_id):
        return self.serializer.get_one(film_id)

    def get_one_by_title(self, film_title):
        return self.serializer.get_one_by_title(film_title)

    def get_random_one_by_genre(self, genre):
        return self.serializer.get_random_one_by_genre(genre)

    def get_all(self):
        return self.serializer.get_all()

    def get_all_by_genre(self, genre):
        return self.serializer.get_all_by_genre(genre)

    def update(self, data):
        self.serializer.update(data)

    def create(self, data):
        Validator.assert_valid_string(data)
        Formatter.format_string(data)

        if self.get_one_by_title(data['title']):
            raise Exception('Фильм с таким названием уже существует!')
        self.serializer.create(data)

    def delete(self, film_id):
        self.serializer.delete(film_id)
