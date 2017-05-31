from flask import render_template

from . import home

@home.route('/')
def index():
    return render_template('home/index.html')

@home.route('/jobs')
def jobs():
    return render_template('home/jobs.html')
