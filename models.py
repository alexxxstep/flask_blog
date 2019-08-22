# from enum import unique
from app import db
from datetime import datetime
import re


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s.lower())


class Task(db.Model):
    # __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f'<Task id: {self.id}, title: {self.title}>'


class Status(db.Model):
    # __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Status id: {self.id}, title: {self.name}>'

#
# class Data(db.Model):
#     # create a table
#     __tablename__ = "data"
#     id = db.Column(db.Integer, primary_key=True)
#     height = db.Column(db.Integer)
#     weight = db.Column(db.Integer)
#     shoesize = db.Column(db.Integer)
#     sex = db.Column(db.String)
#
#     def __init__(self, height, weight, shoesize, sex):
#         self.height = height
#         self.weight = weight
#         self.shoesize = shoesize
#         self.sex = sex
