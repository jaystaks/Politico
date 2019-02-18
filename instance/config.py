import os

class Config:
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    JSON_SORT_KEYS = False

class TestingConfig(Config):
    TESTING = True
    DEBUG = True


appConfig = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
