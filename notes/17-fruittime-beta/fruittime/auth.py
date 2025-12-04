#!/usr/bin/env python3

"""
Fruittime authentication

@author: CS330
@version: 2025.11
"""

from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from fruittime import db, login_manager
from fruittime.forms import LoginForm, SignupForm
from fruittime.models import User

auth = Blueprint("auth", __name__, url_prefix="/")


@auth.route("/signup", methods=["get", "post"])
def signup():
    signup_form = SignupForm()
    if not signup_form.validate_on_submit():
        return render_template("signup.jinja", signup_form=signup_form)
    user = db.session.query(User).filter_by(email=signup_form.email.data).first()
    if user:
        flash("User already exists", "error")
        return redirect(url_for("auth.signup"))
    new_user = User()
    new_user.email = signup_form.email.data
    new_user.password = generate_password_hash(signup_form.password.data)
    new_user.name = signup_form.name.data
    db.session.add(new_user)
    db.session.commit()
    login_user(new_user)
    flash(f"Welcome, {new_user.name}")
    return redirect(url_for("main.index"))


@auth.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm(request.form)
    if not login_form.validate_on_submit():
        return render_template("login.jinja", login_form=login_form)
    user = db.session.query(User).filter_by(email=login_form.email.data).first()
    if not (user and check_password_hash(user.password, login_form.password.data)):
        flash("Please check your login details and try again.")
        return redirect(url_for("auth.login"))
    login_user(user)
    flash(f"Welcome, {user.name}")
    return redirect(url_for("main.index"))


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).filter_by(id=user_id).first()
