class Config: # сюда зачем то передается object
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./movies.db'
    # 'sqlite:///:memory:' перетащить базу в папку instance
    SQLALCHEMY_TRACK_MODIFICATIONS = False

