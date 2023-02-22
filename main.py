from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config):
    application = Flask(__name__)
    application.config.from_object(config)
    register_extensions(application)

    return application


def register_extensions(application):
    db.init_app(application)
    api = Api(app)
    api.add_namespace(movie_ns)  # books
    api.add_namespace(director_ns)  # directors
    api.add_namespace(genre_ns)  # genre


def create_data(app, db):
    with app.app_context():
        db.create_all()

        with db.session.begin():
            db.session.add_all()


app_config = Config()
app = create_app(app_config)
register_extensions(app)

if __name__ == '__main__':

    app.run(host="localhost", port=10001, debug=True)