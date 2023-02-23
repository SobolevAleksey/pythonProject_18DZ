# Консоль 
# python -n venv venv (создает виртуальное окружение) 
# pip install flask flask-restx flask-sqlalchemy ( устанавливаем алхимию) 
# pip install marshmallow (для создания схем) 
# settings - project - python Interpetr - add - Existing -( путь до venv\Scripts\python.exe)
# working directory - указываем нашу папку проекта 
# db файл храниться в папке instance/ ставим галочку в all schemas/ aplly
from flask import Flask
from flask_restx import Api

from config import Config
from setup_db import db
from views.directors import director_ns
from views.genres import genre_ns
from views.movies import movie_ns


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)
    register_extensions(app)
    return app


def register_extensions(app):
    db.init_app(app)
    api = Api(app)  # app
    api.add_namespace(movie_ns)  # books
    api.add_namespace(director_ns)  # directors
    api.add_namespace(genre_ns)  # genre
    create_data(app, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()

        # with db.session.begin():
        # db.session.add_all()


app = create_app(Config())
app.debug = True

if __name__ == '__main__':
    app.run(host="localhost", port=10001, debug=True)
