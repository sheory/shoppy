from flask import Flask, current_app
from flask_migrate import Migrate
from .model import configure as config_db

__DATABASE__ = current_app.config.get('SQLALCHEMY_DATABASE_URI', '')

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = __DATABASE__
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    config_db(app)

    Migrate(app, app.db)

    return app
