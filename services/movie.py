class MovieService:
    def __init__(self, dao):
        self.dao = dao

    def get_one(self, mid):
        return self.dao.get_one(mid)

    def get_all(self):
        return self.dao.get_all()

    def update(self, movie_data): # передается data
        # self.dao.update(data)
        # return self.dao
        
        mid = movie_data.get('id')
        movie = self.dao.get_one(mid)
        if not movie:
            return '', 404

        movie.title = movie_data.get('title')
        movie.description = movie_data.get('description')
        movie.trailer = movie_data.get('trailer')
        movie.year = movie_data.get('year')
        movie.rating = movie_data.get('rating')
        movie.genre_id = movie_data.get('genre_id ')
        movie.director_id = movie_data.get('director_id')

        self.dao.update(movie)

    def create(self, data):
        return self.dao.create(data)

    def delete(self, mid):
        self.dao.delete(mid)
