from flask import Flask
from flask import current_app
from flask import Blueprint

from flask_migrate import Migrate

from .model import configure as config_db

def create_app():
    app = Flask(__name__)

    with app.app_context():
        __DATABASE__ = current_app.config.get('SQLALCHEMY_DATABASE_URI', '')

    app.config['SQLALCHEMY_DATABASE_URI'] = __DATABASE__
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    config_db(app)

    from .modules.product.api import product_blueprint
    app.register_blueprint(product_blueprint)

    Migrate(app, app.db)

    return app

# def get_bp():
#     shoppy = Blueprint('shoppy', __name__)

#     return shoppy
