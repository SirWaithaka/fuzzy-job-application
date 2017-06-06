from flask_wtf import FlaskForm
from wtforms import HiddenField, IntegerField, PasswordField, StringField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo



"""
Forms that will get rendered
"""
class ApplicationForm(FlaskForm):
    """
    Allows users to apply for a position
    """
    age = IntegerField("Age", validators=[DataRequired()])
    skill_set = HiddenField(validators=[DataRequired()])
    submit = SubmitField("Send Application")

class JobPostForm(FlaskForm):
    """
    Allows user to post a job vacancy
    """
    company = StringField("Company Name", validators = [DataRequired()])
    position = StringField('Position', validators = [DataRequired()])
    email = StringField('Email Contacts', validators = [DataRequired(), Email()])
    description = TextAreaField('Job Description', validators = [DataRequired()])
    skill = HiddenField()
    submit = SubmitField('Submit')
