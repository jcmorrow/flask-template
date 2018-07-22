import unittest
from functools import wraps

from app import create_app, db
from config import Config


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/template_test'


app = create_app(TestConfig)


def with_app_context(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        with app.app_context():
            return f(*args, **kwds)
    return wrapper


class FeatureTest(unittest.TestCase):
    @with_app_context
    def setUp(self):
        db.create_all()
        self.client = app.test_client()


class TestVisitRoot(FeatureTest):
    def test_it_says_hello_world(self):
        pass
