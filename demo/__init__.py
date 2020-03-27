from flask_cors import CORS
import connexion
import yaml
from . import extension


def add_file_config(app):
    with open(f'{extension.dir_path}/config.yaml') as f:
        config = yaml.load(f, Loader=yaml.FullLoader)
        app.config.update(config)


def add_sql_alchemy(app):
    extension.db.init_app(app)


def init_app():
    app = connexion.FlaskApp(__name__, specification_dir='./swagger/')
    app.add_api('swagger.yaml')
    CORS(app.app)
    flask_app = app.app
    add_file_config(flask_app)
    add_sql_alchemy(flask_app)
    return flask_app
