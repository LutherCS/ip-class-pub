#!/usr/bin/env python3
"""Flask app"""

from config import app, db
from flask import redirect, render_template, request, url_for
from model import Animal, AnimalSchema, Location, AnimalAddForm


@app.route("/")
def show_zoo():
    """Show animals in the DB"""
    zoo = db.session.query(Animal).all()
    schema = AnimalSchema(many=True)
    return render_template("index.html", zoo=schema.dump(zoo))


@app.get("/add")
def view_add_form() -> str:
    """Display an add animal form"""
    return render_template("add_form.html", form=AnimalAddForm())


@app.post("/add")
def handle_add_form():
    """Add an animal"""
    form = AnimalAddForm(request.form)
    if not form.validate():
        return redirect(url_for("view_add_form"), 302)
    location = Location(name=form.location.data)
    existing_location = db.session.query(Location).filter_by(name=location.name).first()
    if existing_location:
        location = existing_location
    else:
        db.session.add(location)
    animal = Animal()
    animal.name = form.name.data
    animal.age = form.age.data
    animal.species = form.species.data
    animal.location = location
    db.session.add(animal)
    db.session.commit()
    return redirect(url_for("show_zoo"), 302)


@app.route("/delete/<int:animal_id>", methods=["delete", "post"])
def delete_animal(animal_id: int):
    db.session.query(Animal).filter_by(id=animal_id).delete()
    db.session.commit()
    return redirect(url_for("show_zoo"), 302)
