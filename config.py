import os

from dotenv import load_dotenv

try:
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)
except Exception as e:
    pass



class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(12)
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

    UPLOAD_FOLDER = 'app\\uploads'
    ALLOWED_EXTENSIONS = set(['pdf'])


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
