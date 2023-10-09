from flask import render_template, Blueprint, request, url_for, redirect

from src.database.container import filmService
from src.films.utils.film_data_helper import FilmDataHelper

films_blueprint = Blueprint('films_blueprint', __name__, template_folder='templates', static_folder='../static')
filmDataHelper = FilmDataHelper()


@films_blueprint.route("/")
def main():
    raw_films = filmService.get_all()
    films = filmDataHelper.format_films(raw_films)
    return render_template("main.html", films=films)


@films_blueprint.route("/film/<int:film_id>")
def detail_film(film_id):
    raw_film = filmService.get_one(film_id)
    film = filmDataHelper.format_film(raw_film)
    return render_template("detail_film.html", film=film)


@films_blueprint.route('/films_by_genre', methods=['POST'])
def films_by_genre():
    selected_genre = request.form.get('genre')
    raw_films = filmService.get_all_by_genre(selected_genre)
    films = filmDataHelper.format_films(raw_films)
    return render_template('films_by_genre.html', films=films, genre=selected_genre)


@films_blueprint.route('/random_film', methods=['POST'])
def random_film():
    selected_genre = request.form.get('genre')
    film = filmService.get_random_one_by_genre(selected_genre)
    film_id = film.id
    return redirect(url_for("films_blueprint.detail_film", film_id=film_id))

