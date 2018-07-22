from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()


def create_app(config_class=Config):
    app = Flask(__name__)
    Migrate(app, db)

    app.config.from_object(config_class)

    db.init_app(app)

    from app.static import static
    app.register_blueprint(static)

    return app

from app.models.widget import Widget
