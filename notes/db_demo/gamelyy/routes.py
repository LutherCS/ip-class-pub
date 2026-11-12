"""
GamelYY routes

@author: Roman Yasinovskyy
@version: 2026.10
"""

from flask import Blueprint, current_app, redirect, render_template, request, url_for

from gamelyy.logic import get_db

main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def index():
    user = current_app.config["user"]
    db = get_db()
    all_games = db.execute(
        "select * from game join shelf on game.game_id=shelf.game where user=?", (user,)
    ).fetchall()
    return render_template("reviews.jinja", all_games=all_games)


@main.post("/addGame")
def add_game_review():
    user = current_app.config["user"]
    game_title = request.form.get("title", "")
    db = get_db()
    game_id = db.execute("select game_id from game where names=?", (game_title,)).fetchone()[
        "game_id"
    ]
    db.execute("insert into shelf values(?, ?)", (game_id, user))
    db.commit()

    return redirect(url_for("main.index"), code=302)
