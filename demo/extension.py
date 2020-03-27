import os
from flask_sqlalchemy import SQLAlchemy


dir_path = os.path.dirname(os.path.realpath(__file__))
db = SQLAlchemy()