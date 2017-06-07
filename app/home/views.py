import json
import hashlib
from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash

from . import home
from .fuzzy import get_fuzzy_score, get_total_score
from .forms import ApplicationForm, JobPostForm
from .. import db
from ..models import Application, Job, User

@home.route('/')
@login_required
def index():
    return render_template('home/index.html')

@home.route('/applicants')
@login_required
def applicants():
    """
    Return applicants with their fuzzy result
    """

    applicants = []
    job_posts = []
    users_skills = [] # contain skillset of all users

    applications = Application.query.all()
    for application in applications:
        applicant = User.query.get_or_404(application.applicant_id)
        applicants.append(applicant)
        job_post = Job.query.get_or_404(application.job_id)
        job_posts.append(job_post)

        # contains data about the user skills
        user_skill = []
        for key, value in application.expertise.items():
            user_skill.append(value)

        users_skills.append(user_skill)

    users_scores = []
    for skill in users_skills:
        users_scores.append(get_total_score(skill))

    return render_template('home/applicants.html', applicants=applicants, exp=users_scores, job_posts=job_posts, zip=zip)

@home.route('/apply/<int:id>',methods=['GET', 'POST'])
@login_required
def apply(id):
    """
    Apply for selected position
    """
    job = Job.query.get_or_404(id)

    form = ApplicationForm()
    if form.validate_on_submit():
        job_id = id
        age = form.age.data
        applicant_id = current_user.get_id()
        expertise = json.loads(form.skill_set.data)

        application = Application(age=age, expertise=expertise, job_id=job_id, applicant_id=applicant_id)

        db.session.add(application)
        db.session.commit()

        flash("You have successfully applied for this position")

        return redirect(url_for('home.jobs'))

    return render_template('home/apply.html', form=form, job=job)

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

        company = form.company.data
        position = form.position.data
        email = form.email.data
        description = form.description.data
        skills = form.skill.data

        skills = json.loads(skills)

        skill_set_dict = {}
        skill_set_list = []
        for skill in skills:
            skill_set_list.append(skill['skill'])

        for item in skill_set_list:
            hashed = item.encode('utf-8')
            hashed = int(hashlib.md5(hashed).hexdigest()[:8], 16)
            skill_set_dict[hashed] = item

        post = Job(company=company, position=position, email=email, description=description, skills=skill_set_dict)

        db.session.add(post)
        db.session.commit()

        flash("Job vacancy successfully added.")

        # return render_template('home/example.html', skills=skill_set_dict)

        # redirect to jobs page
        return redirect(url_for("home.jobs"))

    return render_template('home/post.html', form=form)
