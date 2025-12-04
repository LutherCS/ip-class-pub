#!/usr/bin/env python3
"""
PandAuth authentication

@author:
@version: 2025.12
"""

import datetime
import json

import requests
from flask import Blueprint, current_app, redirect, request, url_for
from flask_login import login_required, login_user, logout_user

from . import client, db, login_manager
from .models import User

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.get("/login")
def login():
    """Log in"""

    return ""


@auth.route("/login/callback")
def callback():
    """Google callback"""

    return redirect(url_for("main.index"))


@auth.route("/logout")
@login_required
def logout():
    """Log out"""
    logout_user()
    return redirect(url_for("main.index"))


@login_manager.user_loader
def load_user(user_id):
    """User loader"""
    return db.session.query(User).filter_by(id=user_id).first()
