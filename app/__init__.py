# global imports
from flask import Flask

# local imports
from config import app_config

def create_app(config):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config])
    app.config.from_pyfile('config.py')

    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)

    return app
