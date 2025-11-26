#!/usr/bin/env python3

"""
Fruittime routes

@author: CS330
@version: 2025.11
"""

import datetime
from flask import Blueprint, current_app, redirect, render_template, request, url_for

from fruittime import db
from fruittime.logic import get_data
from fruittime.models import Review, ReviewSchema, Fruit

main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def index():
    orchard = db.session.query(Review).all()
    schema = ReviewSchema(many=True)

    return render_template("reviews.jinja", reviews=schema.dump(orchard))


@main.post("/save")
def save_review():
    fruit_name = request.form.get("fruit_name", "")
    fruit_rating = int(request.form.get("fruit_rating", "0"))
    fruit_opinion = request.form.get("fruit_opinion", "")
    fruit = Fruit()
    fruit.name = fruit_name
    existing_fruit = db.session.query(Fruit).filter_by(name=fruit.name).first()
    if existing_fruit:
        fruit = existing_fruit
    else:
        data = get_data(fruit_name)
        if data:
            fruit.family = data["family"]
            fruit.order = data["order"]
            fruit.genus = data["genus"]
            fruit.calories = data["nutritions"]["calories"]
            fruit.sugar = data["nutritions"]["sugar"]
            fruit.fat = data["nutritions"]["fat"]
            fruit.carbohydrates = data["nutritions"]["carbohydrates"]
            fruit.protein = data["nutritions"]["protein"]
        else:
            fruit.calories = 0
            fruit.sugar = 0
            fruit.fat = 0
            fruit.carbohydrates = 0
            fruit.protein = 0
        db.session.add(fruit)
        db.session.commit()
    review = Review()
    review.fruit = fruit
    review.rating = fruit_rating
    review.opinion = fruit_opinion
    review.date = datetime.datetime.now()
    db.session.add(review)
    db.session.commit()
    return redirect(url_for("main.index"))


@main.get("/delete/<int:idx>")
def delete_review(idx: int):
    return redirect(url_for("main.index"))
