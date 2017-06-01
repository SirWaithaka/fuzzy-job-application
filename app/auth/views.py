from flask import flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user


from . import auth
from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import User

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        # check whether user exists in the database
        # check whether password matches database record
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):

            # login user
            login_user(user)

            # redirect user to dashboard
            return redirect(url_for('home.index'))

        # when login details are incorrect
        else:
            flash("Invalid Email or Password. Try again.")

    return render_template('auth/login.html', form=form, title="Login")

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)

        # add user to database
        db.session.add(user)
        db.session.commit()
        flash("You have successfully registered! You may now login.")

        # redirect to the login page
        return redirect(url_for("auth.login"))

    return render_template('auth/register.html', form=form, title="Register")

@auth.route('/logout')
@login_required
def logout():
    """
    Logout users
    """
    logout_user
    flash("You have successfully been logged out.")

    # redirect to the login page
    return redirect(url_for("auth.login"))
