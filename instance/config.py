import os

class Config:
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    JSON_SORT_KEYS = False
    TESTING = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    DATABASE_URI = os.getenv('DATABASE_URL')

class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    DATABASE_URI = os.getenv('DATABASE_URL')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

class TestingConfig(Config):
    TESTING = True
    DEBUG = True


appConfig = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production':ProductionConfig,
}
