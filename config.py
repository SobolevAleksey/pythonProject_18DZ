class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


#     SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' 'sqlite:///movies.db'