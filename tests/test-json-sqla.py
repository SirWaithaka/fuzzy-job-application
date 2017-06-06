import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.mutable import MutableDict
from sqlalchemy.types import TypeDecorator, TEXT


app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy()

db.init_app(app)

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

json_type = MutableDict.as_mutable(JsonEncodedDict)


class TestApplication(db.Model):
    __tablename__ = 'test_application'

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(json_type)

    def __init__(self, data):
        self.data = data


@app.route('/')
def index():
    db.create_all()
    bob = TestApplication({"name": "bob"})

    db.session.add(bob)
    db.session.commit()

    bob.data['surname'] = 'Selbat'
    bob.data['age'] = 5
    # db.session.add(bob)
    db.session.commit()

    return "success"


if __name__ == "__main__":
    app.run(port=7000)
