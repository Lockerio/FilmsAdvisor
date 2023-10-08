import math


class FilmDataHelper:
    @staticmethod
    def count_rating(ratings):
        ratings_amount = len(ratings)
        if ratings_amount == 0:
            current_rating = 0
        else:
            ratings_sum = 0
            for rating in ratings:
                ratings_sum += rating.rating

            current_rating = math.ceil(ratings_sum / ratings_amount)

        return current_rating

    def format_films(self, films):
        formatted_films = []
        for film in films:
            current_id = film.id
            current_title = film.title
            current_genre = film.genre

            ratings = film.ratings
            current_rating = self.count_rating(ratings)

            formatted_films.append({
                "id": current_id,
                "title": current_title,
                "genre": current_genre,
                "rating": current_rating
            })

        sorted_films = sorted(formatted_films, key=lambda x: x['rating'], reverse=True)
        return sorted_films

    def format_film(self, film):
        ratings = film.ratings
        current_rating = self.count_rating(ratings)

        formatted_film = {
            "id": film.id,
            "title": film.title,
            "genre": film.genre,
            "rating": current_rating,
            "comments": [
                {
                    "author": comment.user.first_name + " " + comment.user.last_name,
                    "text": comment.text
                }
                for comment in film.comments
            ]
        }

        return formatted_film
