# global imports
import json
from flask_login import UserMixin
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.types import TypeDecorator, TEXT
from werkzeug.security import generate_password_hash, check_password_hash

# local imports
from app import db, login_manager

class JsonEncodedDict(TypeDecorator):
    """Enables JSON storage by encoding and decoding on the fly."""
    impl = TEXT

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value
JsonType = MutableDict.as_mutable(JsonEncodedDict)

class User(UserMixin, db.Model):
    """
    Create a User table
    """

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(60), index = True, unique = True)
    username = db.Column(db.String(60), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    applications = db.relationship('Application', backref = 'vacancy', lazy='dynamic')

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return "<User: {}>".format(self.username)


class Job(db.Model):
    """
    Create a Job Post table
    """

    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key = True)
    company = db.Column(db.String(60), index = True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    position = db.Column(db.String(60), index = True, nullable=False)
    email = db.Column(db.String(60), index = True, nullable=False)
    skills = db.Column(JsonType, nullable=False)
    applications = db.relationship('Application', backref = 'job', lazy='dynamic')

    def __repr__(self):
        return '<Job {}>'.format(self.position)



class Application(db.Model):

    __tablename__ = "applications"

    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer, index = True, nullable=False)
    applicant_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'))
    expertise = db.Column(JsonType, nullable=False)


    def __repr__(self):
        return "<Application {}>".format(self.id)

#
# class Skills(db.Model):
#     """
#     Create Skills table
#     """
#
#     __tablename__ = 'skills'
#
#     id = db.Column(db.Integer, primary_key = True)
#     data = db.Column(JsonType, nullable=False)
#     # applicant_id = db.relationship('Application', backref='skills', lazy='dynamic')
#
#     def __init__(self, data):
#         self.data = data
#
#     def __repr__(self):
#         return '<Skills> %s' % (self.data)
#

# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
