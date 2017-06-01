from flask import render_template
from flask_login import current_user, login_required

from . import home

@home.route('/')
@login_required
def index():
    return render_template('home/index.html')

@home.route('/jobs')
@login_required
def jobs():
    return render_template('home/jobs.html')
