from flask import Blueprint
from jinja2 import Template, Environment, FileSystemLoader

from demo.extension import get_template

people_blueprint = Blueprint('people', __name__, url_prefix='/people')


from demo.extension import db
from demo.models.models import User


def read():
    session = db.session
    session.execute(User)
    return 'read success'


@people_blueprint.route('/', methods=('GET', 'POST'))
def render():
    persons = [
        {'name': 'Andrej', 'age': 34},
        {'name': 'Mark', 'age': 17},
        {'name': 'Thomas', 'age': 44},
        {'name': 'Lucy', 'age': 14},
        {'name': 'Robert', 'age': 23},
        {'name': 'Dragomir', 'age': 54},
    ]
    template = get_template('showminors.html')
    return template.render(persons=persons)
