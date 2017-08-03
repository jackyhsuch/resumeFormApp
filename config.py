import os
import urllib.parse as urlparse

from dotenv import load_dotenv

try:
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path)
except:
    pass



class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.urandom(12)

    UPLOAD_FOLDER = 'app\\uploads'
    ALLOWED_EXTENSIONS = set(['pdf'])

    IS_PROD = int(os.environ['IS_PROD'])
    PORT = int(os.environ.get('PORT', 5000))

    if IS_PROD:
        url = urlparse.urlparse(os.environ['DATABASE_URL'])
        SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://"+url.username+":"+url.password+"@"+url.hostname+":"+str(url.port)+"/"+url.path[1:]
    else:
        DEBUG = True
        SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEBUG = True


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


class LocalConfig(Config):
    DEBUG = True
