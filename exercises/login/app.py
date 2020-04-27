from flask import Flask, session, redirect, url_for, escape, request, render_template
import os


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    raise NotImplementedError


@app.route("/login", methods=["GET", "POST"])
def login():
    raise NotImplementedError


@app.route("/logout", methods=["POST"])
def logout():
    raise NotImplementedError
