#!/usr/bin/env python3
"""
Tech market navigator forms

@authors: Roman Yasinovskyy
@version: 2024.11
"""

from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])


class SignupForm(LoginForm):
    name = StringField("Name", validators=[DataRequired()])
