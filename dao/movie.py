from dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        return self.session.query(Movie).get(mid)

    def get_all(self, filters):
        if filters['director_id']:
            return self.session.query(Movie).filter(Movie.director_id == filters['director_id']).all()
        if filters['genre_id']:
            return self.session.query(Movie).filter(Movie.genre_id == filters['genre_id']).all()
        if filters['year']:
            return self.session.query(Movie).filter(Movie.year == filters['year']).all()

        return self.session.query(Movie).all()
    
    def update(self, data):
        mid = data.pop('id')
        movie = self.get_one(mid)
        for field_name, field_value in data.items():
            setattr(movie, field_name, field_value)
            ## вместо movie.name = data['name']
        
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


        self.session.delete(movie)
        self.session.sommit()
