from dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self):
        movie_list = self.session.query(Movie)
        return movie_list

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()

        return movie

    def create(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.commit()

        return movie

    def delete(self, mid):
        movie = self.session.query(Movie).get(mid)
        if not movie:
            return '', 404

        self.session.delete(movie)
        self.session.sommit()
