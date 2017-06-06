from flask import Flask, render_template, request, url_for
from flask_bootstrap import Bootstrap
from flask_mongoengine import MongoEngine
from flask_mongoengine.wtf import model_form
from wtforms.validators import InputRequired


db = MongoEngine()

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')

db.init_app(app)
Bootstrap(app)

class User(db.Document):
    email = db.StringField(required=True)
    first_name = db.StringField(max_length=50)
    last_name = db.StringField(max_length=50)

class Content(db.EmbeddedDocument):
    text = db.StringField()
    lang = db.StringField(max_length=3)

class Post(db.Document):
    title = db.StringField(max_length=120, required=True, validators=[InputRequired(message='Missing title.')])
    author = db.ReferenceField(User)
    tags = db.ListField(db.StringField(max_length=30))
    content = db.EmbeddedDocumentField(Content)

PostForm = model_form(Post)

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = PostForm(request.form)
    if request.method == 'POST' and form.validate():
        # do something
        redirect('done')
    return render_template('add_post.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)
