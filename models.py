from flask_sqlalchemy import SQLAlchemy
from main import app

db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(64), primary_key=False, unique=True, nullable=False)
    password = db.Column(db.String(64), primary_key=False, unique=False, nullable=False)


class Themes(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    name = db.Column(db.String(64), primary_key=False, unique=True, nullable=False)
    shortname = db.Column(db.String(64), primary_key=False, unique=True, nullable=False)
    description = db.Column(db.String(256), primary_key=False, unique=False, nullable=False)
    text = db.Column(db.String(4096), primary_key=False, unique=False, nullable=False)


class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    theme = db.Column(db.Integer, db.ForeignKey('themes.id'), primary_key=False, unique=False, nullable=False)
    text = db.Column(db.String(4096), primary_key=False, unique=False, nullable=False)
    answer = db.Column(db.Float, primary_key=False, unique=False, nullable=False)


class Learned(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), primary_key=False, unique=False, nullable=False)
    theme = db.Column(db.Integer, db.ForeignKey('themes.id'), primary_key=False, unique=False, nullable=False)


class Variants(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    is_theme = db.Column(db.Boolean, primary_key=False, unique=False, nullable=False)
    theme = db.Column(db.Integer, db.ForeignKey('themes.id'), primary_key=False, unique=False, nullable=True)


class TasksInVariants(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    task = db.Column(db.Integer, db.ForeignKey('tasks.id'), primary_key=False, unique=False, nullable=False)
    variant = db.Column(db.Integer, db.ForeignKey('variants.id'), primary_key=False, unique=False, nullable=False)
    position = db.Column(db.Integer, primary_key=False, unique=False, nullable=False)