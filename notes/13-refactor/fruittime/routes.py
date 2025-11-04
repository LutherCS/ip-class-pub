#!/usr/bin/env python3

"""
Fruittime routes

@author: CS330
@version: 2025.11
"""

from flask import current_app, redirect, render_template, request, Blueprint, url_for
from .logic import get_data

main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def index():
    return render_template("reviews.jinja")


@main.post("/save")
def save_review():
    fruit_name = request.form.get("fruit_name", "")
    fruit_rating = int(request.form.get("fruit_rating", "0"))
    fruit_opinion = request.form.get("fruit_opinion", "")
    data = get_data(fruit_name)
    if data:
        fruit_nutrition = data["nutritions"]
    else:
        fruit_nutrition = {
            "calories": 0,
            "carbs": 0,
            "fat": 0,
            "protein": 0,
            "sugar": 0,
        }
    current_app.config["REVIEWS"].add(
        {
            "name": fruit_name,
            "rating": fruit_rating,
            "opinion": fruit_opinion,
            "nutrition": fruit_nutrition,
        }
    )
    return redirect(url_for("main.index"))


@main.get("/delete/<int:idx>")
def delete_review(idx: int):
    current_app.config["REVIEWS"].remove(idx)
    return redirect(url_for("main.index"))
