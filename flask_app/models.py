from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role = db.Column(db.String(20), default='scorer')  # admin, scorer, viewer
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    categories = db.relationship('Category', backref='event', lazy=True, cascade='all, delete-orphan')


class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)  # e.g. "Under 10 Girls"
    piece_type = db.Column(db.String(10), default='5P')  # 5P or 4P
    event_id = db.Column(db.Integer, db.ForeignKey('events.id'), nullable=False)
    groups = db.relationship('SchoolGroup', backref='category', lazy=True, cascade='all, delete-orphan')


class School(db.Model):
    __tablename__ = 'schools'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=True)


class SchoolGroup(db.Model):
    """A school's entry in a category (the team)."""
    __tablename__ = 'school_groups'
    id = db.Column(db.Integer, primary_key=True)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    # Team totals (auto-calculated, stored for quick access)
    team_set_vault = db.Column(db.Float, default=0)
    team_vol_vault = db.Column(db.Float, default=0)
    team_set_floor = db.Column(db.Float, default=0)
    team_vol_floor = db.Column(db.Float, default=0)
    team_total = db.Column(db.Float, default=0)
    team_position = db.Column(db.Integer, default=0)
    # Group score & position
    group_score = db.Column(db.Float, default=0)
    group_position = db.Column(db.Integer, default=0)

    school = db.relationship('School', backref='groups')
    athletes = db.relationship('Athlete', backref='school_group', lazy=True,
                               cascade='all, delete-orphan', order_by='Athlete.number')


class Athlete(db.Model):
    __tablename__ = 'athletes'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(150), default='')
    school_group_id = db.Column(db.Integer, db.ForeignKey('school_groups.id'), nullable=False)
    scores = db.relationship('Score', backref='athlete', uselist=False,
                             cascade='all, delete-orphan')


class Score(db.Model):
    __tablename__ = 'scores'
    id = db.Column(db.Integer, primary_key=True)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athletes.id'), nullable=False)
    set_vault = db.Column(db.Float, default=0.0)
    vol_vault = db.Column(db.Float, default=0.0)
    set_floor = db.Column(db.Float, default=0.0)
    vol_floor = db.Column(db.Float, default=0.0)
    # For 5-piece only:
    set_vault_2 = db.Column(db.Float, default=0.0)  # not used in 4P

    @property
    def total(self):
        return round(self.set_vault + self.vol_vault + self.set_floor + self.vol_floor, 2)

    individual_total = db.Column(db.Float, default=0.0)
    individual_position = db.Column(db.Integer, default=0)
