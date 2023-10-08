from flask import Flask

from src.films.views import films_blueprint

app = Flask(__name__)
app.register_blueprint(films_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
