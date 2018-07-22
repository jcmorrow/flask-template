import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
flask_env = os.environ.get('FLASK_ENV')
load_dotenv(os.path.join(basedir, '.env'))

if flask_env:
    load_dotenv(os.path.join(basedir, '.env.{}'.format(flask_env)))
    if flask_env == 'development':
        load_dotenv(os.path.join(basedir, '.env.local'))


def get_from_env(key, default=None):
    return os.environ.get(key, default)


def require_from_env(key):
    return os.environ[key]


class Config:
    SECRET_KEY = require_from_env('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = get_from_env('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = get_from_env(
        'SQLALCHEMY_TRACK_MODIFICATIONS', False)
    LOG_TO_STDOUT = get_from_env('LOG_TO_STDOUT')
