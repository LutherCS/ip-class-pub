#!/usr/bin/env python3

"""
Fruittime routes

@author: CS330
@version: 2025.11
"""

import datetime

from flask import Blueprint, current_app, flash, redirect, render_template, request, url_for, g
from flask_login import current_user, login_required
from sqlalchemy import func, select

from fruittime import db
from fruittime.forms import NewReviewForm
from fruittime.logic import get_data
from fruittime.models import Fruit, Review, ReviewSchema, Vote

main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def index():
    orchard = db.session.query(Review).all()
    schema = ReviewSchema(many=True)
    g.review_votes = {}
    g.user_votes = []
    try:
        review_votes = db.session.execute(
            select(Vote.review_id, func.count(Vote.user_id).label("count"))
            .join(Review)
            .filter_by(author_id=current_user.id)
            .group_by(Vote.review_id)
        ).all()
        g.review_votes = dict(review_votes)
        user_votes = db.session.scalars(
            select(Vote.review_id).where(Vote.user_id == current_user.id)
        ).all()
        g.user_votes = user_votes
    except AttributeError as attrib_err:
        pass

    return render_template(
        "reviews.jinja", reviews=schema.dump(orchard), review_form=NewReviewForm()
    )


@main.post("/save")
def save_review():
    form = NewReviewForm(request.form)
    if not form.validate_on_submit():
        flash("Please support your rating with a valid opinion", "warning")
        return redirect(url_for("main.index"), 302)
    if not (form.name.data and form.rating.data and form.opinion.data):
        flash("Please support your rating with a valid opinion", "warning")
        return redirect(url_for("main.index"), 302)
    fruit = Fruit()
    fruit.name = form.name.data
    existing_fruit = db.session.query(Fruit).filter_by(name=fruit.name).first()
    if existing_fruit:
        fruit = existing_fruit
    else:
        data = get_data(fruit.name)
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
    review = Review()
    review.rating = form.rating.data
    review.opinion = form.opinion.data
    review.fruit = fruit
    review.date = datetime.datetime.now()
    if current_user.is_authenticated:
        review.author_id = current_user.id

    db.session.add(review)
    db.session.commit()
    return redirect(url_for("main.index"), code=302)


@main.get("/delete/<int:review_id>")
def delete_review(review_id: int):
    db.session.query(Review).filter_by(id=review_id).delete()
    db.session.commit()
    return redirect(request.referrer)


@main.post("/upvote/<int:review_id>")
def upvote_review(review_id: int):
    vote = db.session.query(Vote).filter_by(user_id=current_user.id, review_id=review_id).first()
    if vote:
        db.session.delete(vote)
    else:
        new_vote = Vote()
        new_vote.user_id = current_user.id
        new_vote.review_id = review_id
        db.session.add(new_vote)
    db.session.commit()
    return redirect(request.referrer)
