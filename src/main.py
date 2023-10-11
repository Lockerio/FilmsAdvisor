from flask import Flask

from src.film.views import film_blueprint
from src.user.views import user_blueprint

app = Flask(__name__)
app.register_blueprint(film_blueprint)
app.register_blueprint(user_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
