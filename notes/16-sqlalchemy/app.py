#!/usr/bin/env python3
"""Simple Flask app"""

from flask import render_template
from models import Animal, AnimalSchema

from config import app

@app.route("/")
def show_zoo():
    """Show zoo"""
    zoo = Animal.query.all()
    animal_schema = AnimalSchema(many=True)
    return render_template("index.html", zoo=animal_schema.dump(zoo))


if __name__ == "__main__":
    app.run()
