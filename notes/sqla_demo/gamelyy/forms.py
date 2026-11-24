"""
GamelYY model

@author: Roman Yasinovskyy
@version: 2026.11
"""

from flask_wtf import FlaskForm
from wtforms import EmailField, StringField, PasswordField, RadioField
from wtforms.validators import DataRequired, Email


class NewGameForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])
    rating = RadioField("Rating", choices=[(1, "Rotten"), (2, "Poor"), (3, "OK"), (4, "Awesome")])


class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])


class SignupForm(LoginForm):
    email = EmailField("Email", validators=[Email()])
    confirmation = PasswordField("Confirm Password", validators=[DataRequired()])
