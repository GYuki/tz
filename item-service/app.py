from flask import Flask

from database import db
from extensions import migrate, seeder
from src.views import blueprint


class Config(object):
    SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///items.sqlite3'


def create_app(config_object=Config):
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_extensions(app)
    register_blueprints(app)
    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    seeder.init_app(app, db)


def register_blueprints(app):
    app.register_blueprint(blueprint)


app = create_app(Config)
