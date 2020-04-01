from flask import send_from_directory
from flask_cors import CORS
import connexion
import yaml

from . import extension


from demo.api.people import people_blueprint


def add_file_config(app):
    with open(f'{extension.dir_path}/config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        app.config.update(config)


def connect_sql_database(app):
    extension.db.init_app(app)


def register_blueprint(app):
    app.register_blueprint(people_blueprint)


def init_app():
    app = connexion.FlaskApp(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml')
    CORS(app.app)
    flask_app = app.app
    add_file_config(flask_app)
    register_blueprint(flask_app)
    # connect_sql_database(flask_app)
    return flask_app
