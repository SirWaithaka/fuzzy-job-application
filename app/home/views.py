from flask import flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from . import home
from .forms import JobPostForm
from .. import db
from ..models import Job

@home.route('/')
@login_required
def index():
    return render_template('home/index.html')

@home.route('/apply/<int:id>',methods=['GET', 'POST'])
@login_required
def apply(id):
    """
    Apply for selected position
    """
    job = Job.query.get_or_404(id)


    return render_template('home/apply.html', job=job)

@home.route('/jobs')
@login_required
def jobs():
    # get all rows
    jobs = Job.query.all()

    return render_template('home/jobs.html', jobs=jobs)

@home.route('/post', methods = ['GET', 'POST'])
def post():
    form = JobPostForm()
    if form.validate_on_submit():
        post = Job(description=form.description.data, position=form.position.data, email=form.email.data)

        # add new vacancy to database
        db.session.add(post)
        db.session.commit()
        flash("You have successfully added a job vacancy post.")

        #redirect to jobs page
        return redirect(url_for("home.jobs"))

    return render_template('home/post.html', form=form)
