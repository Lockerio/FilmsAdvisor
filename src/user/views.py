from flask import Blueprint, render_template, request, redirect, url_for

from src.database.container import userService


user_blueprint = Blueprint('user_blueprint', __name__, template_folder='templates', static_folder='static')


@user_blueprint.route('/create_user')
def create_user():
    return render_template('create_user.html')


@user_blueprint.route('/finish_user_creation')
def finish_user_creation():
    try:
        user_to_create_data = {
            'first_name': request.form.get('first_name'),
            'last_name': request.form.get('last_name'),
            'email': request.form.get('email'),
            'password': request.form.get('password')
        }
        userService.create(user_to_create_data)
    except Exception as e:
        return render_template('create_film.html', error_message=e)

    return redirect(url_for('films_blueprint.detail_film', film_id=film_id))


