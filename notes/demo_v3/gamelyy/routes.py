"""
GamelYY routes

@author: Roman Yasinovskyy
@version: 2026.10
"""

from flask import Blueprint, current_app, render_template, request

from gamelyy.logic import game_lookup

main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def index():
    return render_template("index.jinja", all_games=[])


@main.post("/addGame")
def add_game_review():
    the_game = game_lookup(request.form.get("title", ""))
    current_app.config["SHELF"].add(the_game)
    return render_template("reviews.jinja", all_games=current_app.config["SHELF"])
