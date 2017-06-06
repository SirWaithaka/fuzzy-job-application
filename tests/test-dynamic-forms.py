from flask import Flask, flash, render_template
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

SECRET_KEY="development"

app = Flask(__name__)
app.config.from_object(__name__)

Bootstrap(app)

class JobPostForm(FlaskForm):
    """
    Allows user to post a job vacancy
    """
    company = StringField("Company Name", validators = [DataRequired()])
    position = StringField('Position', validators = [DataRequired()])
    email = StringField('Email Contacts', validators = [DataRequired(), Email()])
    description = TextAreaField('Job Description', validators = [DataRequired()])
    submit = SubmitField('Submit')

@app.route('/')
def index(request):


    return render_template('example.html', form=form)

if __name__ == "__main__":
    app.run(port=6001)
