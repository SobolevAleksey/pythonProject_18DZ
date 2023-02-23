class Config: # сюда зачем то передается object
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' # 'sqlite:///./movies.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


#     SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' 'sqlite:///movies.db'
