#!/usr/bin/env python3

import os
from flask import Flask, render_template, redirect, session, request, url_for
from markupsafe import escape

app = Flask(__name__)

app.config.update(SECRET_KEY=os.environ.get("SECRET_KEY"))


@app.route("/")
def index():
    """Main page"""
    if "username" in session:
        return render_template("index.html", username=escape(session.get("username")))
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Login"""
    if request.method == "POST":
        session["username"] = request.form["username"]
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    """Logout"""
    session.pop("username", None)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
