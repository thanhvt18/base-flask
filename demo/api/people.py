from demo.extension import db
from demo.models.models import User


def read():
    session = db.session
    session.execute(User)
    return 'read success'