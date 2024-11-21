#!/usr/bin/env python3
"""Flask app"""

from config import app, db
from flask import redirect, render_template, request, url_for
from model import Animal, AnimalSchema, Location


@app.route("/")
def show_zoo():
    """Show animals in the DB"""
    return render_template("index.html")


@app.get("/add")
def view_add_form() -> str:
    """Display an add animal form"""
    return render_template("add_form.html")


@app.post("/add")
def handle_add_form():
    """Add an animal"""
    return redirect(url_for("show_zoo"), 302)


@app.route("/delete/<int:animal_id>", methods=["delete"])
def delete_animal(animal_id: int):
    return redirect(url_for("show_zoo"), 302)
