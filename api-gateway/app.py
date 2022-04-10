from flask import Flask
from src.views import blueprint


class Config(object):
    SECRET_KEY = 'secret'
    JWT_AUTH_USERNAME_KEY = 'user'
    JWT_AUTH_HEADER_PREFIX = 'Token'
    PORT = 80


def create_app(config_object=Config):
    app = Flask(__name__.split('.')[0])
    app.url_map.strict_slashes = False
    app.config.from_object(config_object)
    register_blueprints(app)
    return app


def register_blueprints(app):
    app.register_blueprint(blueprint)


app = create_app(Config)
