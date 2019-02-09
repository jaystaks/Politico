import os

class Config:
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True

class TestingConfig(Config):
    TESTING = True
    DEBUG = True


appConfig = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
}
