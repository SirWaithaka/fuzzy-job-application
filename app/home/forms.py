from flask_wtf import FlaskForm
from wtforms import FieldList, FormField, PasswordField, StringField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

"""
Miniature forms used in FormField
"""
class RolesForm(FlaskForm):
    role = StringField('Role Description', validators = [DataRequired()])


"""
Forms that will get rendered
"""
class ApplicationForm(FlaskForm):
    """
    Allows users to apply for a position
    """

class JobPostForm(FlaskForm):
    """
    Allows user to post a job vacancy
    """
    company = StringField("Company Name", validators = [DataRequired()])
    position = StringField('Position', validators = [DataRequired()])
    email = StringField('Email Contacts', validators = [DataRequired(), Email()])
    description = TextAreaField('Job Description', validators = [DataRequired()])
    submit = SubmitField('Submit')
