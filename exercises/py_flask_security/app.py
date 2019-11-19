from flask import Flask, session, redirect, url_for, escape, request, render_template

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


@app.route("/")
def index():
    pass


@app.route("/login", methods=["GET", "POST"])
def login():
    pass


@app.route("/logout", methods=["POST"])
def logout():
    pass
