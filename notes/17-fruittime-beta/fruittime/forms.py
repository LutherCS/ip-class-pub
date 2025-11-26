#!/usr/bin/env python3

"""
Fruittime forms

@author: CS330
@version: 2025.11
"""

from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, RadioField, StringField, TextAreaField
from wtforms.validators import DataRequired


class NewReviewForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    rating = RadioField(
        "Rating",
        choices=[(1, "Bad"), (2, "OK"), (3, "Good"), (4, "Excellent")],
        validators=[DataRequired()],
    )
    opinion = TextAreaField("Opinion", validators=[DataRequired()])


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])


class SignupForm(LoginForm):
    name = StringField("Full name", validators=[DataRequired()])
