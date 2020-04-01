from flask import Blueprint, send_from_directory

static_blueprint = Blueprint('static', __name__, url_prefix='/static')


@static_blueprint.route('/<path:path>')
def send_js(path):
    return send_from_directory('static', path)