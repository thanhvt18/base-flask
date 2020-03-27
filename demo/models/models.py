from demo.extension import db
import sqlalchemy
from abc import ABC, abstractmethod


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class ObjectDemo:
    def __init__(self, id):
        print('object demo call')
        self.id = id


class People(ObjectDemo):
    def __init__(self, name, age):
        print(' peole call')
        ObjectDemo.__init__(self, 1)
        self.name = name
        self.age = age

    def get_name(self):
        print(self.name)

    def print_all_attr(self):
        print(self.name, self.age)


class Swing(ObjectDemo):
    def __init__(self, type_swing):
        print('swing call')
        ObjectDemo.__init__(self, 2)
        self.type_swing = type_swing

    def get_type(self):
        print(self.type_swing)

    def print_all_attr(self):
        print(self.type_swing)


class Student(Swing, People):
    def __init__(self, name, age, type_swing):
        People.__init__(self, name, age)
        Swing.__init__(self, type_swing)
        print('object student call')
        print(Student.__mro__)


if __name__ == '__main__':
    student = Student('vu tien thanh', 24, 'ft')
    student.print_all_attr()