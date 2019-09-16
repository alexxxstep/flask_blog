# from enum import unique
from app import db
from datetime import datetime
import re

from flask_security import UserMixin, RoleMixin


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s.lower())


task_tags = db.Table('task_tags',
                     db.Column('task_id', db.Integer, db.ForeignKey('task.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                     )


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False, index=True)
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())
    status_id = db.Column(db.Integer, db.ForeignKey('status.id'))

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        self.generate_slug()

    tags = db.relationship('Tag', secondary=task_tags, backref=db.backref('tasks', lazy='dynamic'))

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return f'<Task id: {self.id}, title: {self.title}>'


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __init__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return f'{self.name}'


status_list = ['new', 'in_work', 'finished', 'closed', 'cancelled']


class Status(db.Model):
    __tablename__ = 'status'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)

    def __init__(self, *args, **kwargs):
        super(Status, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'<Status: {self.name}>'


# FLASK SECURITY
roles_users = db.Table('roles_users',
                       db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                       db.Column('role_id', db.Integer(), db.ForeignKey('role.id')),
                       )


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary=roles_users, backref=db.backref('users', lazy='dynamic'))


class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(255))
