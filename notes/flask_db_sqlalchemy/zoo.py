from flask import render_template
from config import app
from models import Animal, AnimalSchema


@app.route("/")
def show_zoo():
    zoo = Animal.query.all()
    animal_schema = AnimalSchema(many=True)
    return render_template("index.html", zoo=animal_schema.dump(zoo))
