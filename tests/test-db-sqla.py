from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy()

db.init_app(app)

class Job(db.Model):
    """
    Create a Job Post table
    """

    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.Text)
    position = db.Column(db.String(60), index = True)
    email = db.Column(db.String(60), index = True)

    def __repr__(self):
        return '<Job {}>'.format(self.position)


@app.route('/')
def index():
    return "Hello"


if __name__ == "__main__":
    app.run(port=6001)
