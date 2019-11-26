from flask import render_template
from config import app
from models import Animal, AnimalSchema


@app.route("/")
def show_zoo():
    pass
