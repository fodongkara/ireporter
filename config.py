import os

class Config(object):
    DEBUG=True
    TESTING=False

class DevelopmentConfig(Config):
    DEVELOPENT=True

class ProductionConfig(Config):
    DEBUG=False

class TestingConfig(Config):
    TESTING=True

runtime_mode = os.environ.get("APP_SETTINGS").strip('"')
env_config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig
}