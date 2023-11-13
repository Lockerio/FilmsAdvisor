from flask import Blueprint, render_template

authentication_blueprint = Blueprint('authentication_blueprint', __name__, template_folder='templates', static_folder='static')


@authentication_blueprint.route('/sign_in')
def sign_in():
    return render_template('sign_in.html')
