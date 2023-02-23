# Консоль 
# python -n venv venv (создает виртуальное окружение) 
# pip install flask flask-restx flask-sqlalchemy ( устанавливаем алхимию) 
# pip install marshmallow (для создания схем) 
# settings - project - python Interpetr - add - Existing -( путь до venv\Scripts\python.exe)
# working directory - указываем нашу папку проекта 
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
    application.app_context().push()
    # configure_app(application)

    return application


def configure_app(application):
    db.init_app(application)
    api = Api(app) # application
    api.add_namespace(movie_ns)  # books
    api.add_namespace(director_ns)  # directors
    api.add_namespace(genre_ns)  # genre


def create_data(app, db):
    with app.app_context():
        db.create_all()

        with db.session.begin():
            db.session.add_all()




if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    configure_app(app)
    app.run(host="localhost", port=10001)
