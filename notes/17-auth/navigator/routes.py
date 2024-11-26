#!/usr/bin/env python3
"""
Tech market navigator routes

@authors: Roman Yasinovskyy
@version: 2024.11
"""

from flask import Blueprint, redirect, render_template, url_for, request
from flask_login import current_user, login_required

from navigator import db
from navigator.models import Company, CompanySchema, Favorite

main = Blueprint("main", __name__, url_prefix="/")


@main.route("/")
def index():
    selected = []
    schema = CompanySchema(many=True)
    if current_user.is_authenticated:
        selected = (
            db.session.query(Favorite.company_id)
            .filter(Favorite.user_id == current_user.id)
            .all()
        )
    data = db.session.query(Company).all()
    return render_template(
        "index.html", data=schema.dump(data), selected=[c[0] for c in selected]
    )


@main.post("/like/<int:company_id>")
@login_required
def likeit(company_id: str):
    existing_favorite = (
        db.session.query(Favorite)
        .filter_by(user_id=current_user.id, company_id=company_id)
        .first()
    )
    if not existing_favorite:
        favorite = Favorite()
        favorite.company_id = company_id
        favorite.user_id = current_user.id
        db.session.add(favorite)
        db.session.commit()
    return redirect(url_for("main.index"))


@main.post("/dislike/<int:company_id>")
@login_required
def dislikeit(company_id: str):
    existing_favorite = (
        db.session.query(Favorite)
        .filter_by(user_id=current_user.id, company_id=company_id)
        .first()
    )
    db.session.delete(existing_favorite)
    db.session.commit()
    if request.form.get("profile"):
        return redirect(url_for("main.profile"))
    return redirect(url_for("main.index"))


@main.get("/profile")
@login_required
def profile():
    schema = CompanySchema(many=True)
    data = (
        db.session.query(Company)
        .join(Favorite)
        .filter(Favorite.user_id == current_user.id)
        .all()
    )
    return render_template("profile.html", data=schema.dump(data))
