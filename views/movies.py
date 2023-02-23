from flask import request
from flask_restx import Resource, Namespace

from container import movie_service
from dao.models.movie import MovieSchema, Movie

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        # movies = movie_service.get_all()
        # result = movies_schema.dump(movies)
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        year = request.args.get('year')
        stmt = movie_service.get_all()
        if director_id:
            stmt = stmt.filter(Movie.director_id == director_id)
        if genre_id:
            stmt = stmt.filter(Movie.genre_id == genre_id)
        if year:
            stmt = stmt.filter(Movie.year == year)
        movies = stmt.all()
        return movies_schema.dump(movies), 200

    def post(self):
        movie_data = request.json
        movie_service.create(movie_data)

        return '', 201


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid: int):
        movie = movie_service.get_one(mid)
        if not movie:
            return '', 404

        return movie_schema.dump(movie), 200

    def put(self, mid: int):
        movie_data = request.json
        movie_data['id'] = mid
        movie = movie_service.update(movie_data)
        return '', 204

    def delete(self, mid: int):
        movie = movie_service.delete(mid)

        return '', 204
