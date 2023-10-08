from flask import render_template, Blueprint

from src.database.container import filmService
from src.films.utils.film_data_helper import FilmDataHelper

films_blueprint = Blueprint('films_blueprint', __name__, template_folder='templates', static_folder='../static')
filmDataHelper = FilmDataHelper()


@films_blueprint.route('/films/<int:film_id>')
def film(film_id):
    raw_film = filmService.get_one(film_id)
    film = filmDataHelper.format_film(raw_film)
    return render_template("detail_film.html", film=film)
