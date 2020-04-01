import os
from flask_sqlalchemy import SQLAlchemy
from jinja2 import Template, Environment, FileSystemLoader

dir_path = os.path.dirname(os.path.realpath(__file__))
db = SQLAlchemy()


def get_template(template_path):
    file_loader = FileSystemLoader('static/template')
    env = Environment(loader=file_loader)
    env.trim_blocks = True
    env.lstrip_blocks = True
    env.rstrip_blocks = True
    return  env.get_template(template_path)