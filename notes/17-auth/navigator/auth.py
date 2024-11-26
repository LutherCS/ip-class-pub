#!/usr/bin/env python3
"""
Tech market navigator authentication routes

@authors: Roman Yasinovskyy
@version: 2024.11
"""

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_login import login_required, login_user, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from navigator import db, login_manager
from navigator.forms import LoginForm, SignupForm
from navigator.models import User

auth = Blueprint("auth", __name__, url_prefix="/")


@auth.route("/signup", methods=["GET", "POST"])
def signup():
    form = SignupForm(request.form)
    if not form.validate_on_submit():
        return render_template("signup.html", form=form)
    user = db.session.query(User).filter_by(email=form.email.data).first()
    if user:
        flash("User already exists")
        return redirect(url_for("auth.signup"))
    new_user = User()
    new_user.email = form.email.data
    new_user.name = form.name.data
    new_user.password = generate_password_hash(form.password.data)
    db.session.add(new_user)
    db.session.commit()
    return redirect(url_for("auth.login"))


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if not form.validate_on_submit():
        return render_template("login.html", form=form)
    user = db.session.query(User).filter_by(email=form.email.data).first()
    if not user or not check_password_hash(user.password, form.password.data):
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
