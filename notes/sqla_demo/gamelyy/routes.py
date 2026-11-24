"""
GamelYY routes

@author: Roman Yasinovskyy
@version: 2026.11
"""

from flask import Blueprint, redirect, render_template, request, url_for
from sqlalchemy import select

from gamelyy import db
from gamelyy.model import Game, GameSchema, Ownership, User
from gamelyy.forms import NewGameForm

main = Blueprint("main", __name__, url_prefix="/")


@main.get("/")
def index():
    """Retrieve all games of a specific user

    Using explicit statement"""
    stmt = (
        select(Game).join(Ownership.game).join(Ownership.user).where(User.username == "anonymous")
    )
    all_games = db.session.scalars(stmt).all()
    print(all_games)
    return render_template("reviews.jinja", all_games=all_games, new_game=NewGameForm())


@main.post("/add")
def add_game():
    """Add an ownership record

    Using filter method"""
    the_user = db.session.scalars(select(User).filter(User.username == "anonymous")).one()
    the_game = db.session.scalars(
        select(Game).filter(Game.names == request.form.get("title", ""))
    ).one()
    ownership = Ownership()
    ownership.game = the_game
    ownership.user = the_user
    db.session.add(ownership)
    db.session.commit()
    return redirect(url_for("main.index"), code=302)


@main.get("/view/<int:game_id>")
def view_game(game_id: int):
    """View the game as JSON

    Using filter_by method"""
    return GameSchema().dumps(db.session.scalars(select(Game).filter_by(game_id=game_id)).one())


@main.get("/update/<int:game_id>")
def update_game(game_id: int):
    """Update number of game owners

    Using first instead of one
    """
    the_game = db.session.scalars(select(Game).where(Game.game_id == game_id)).first()
    if the_game:
        the_game.owned += 1
        db.session.commit()
    return redirect(url_for("main.index"), code=302)


@main.get("/delete/<int:game_id>")
def delete_game(game_id: int):
    """Delete an ownership record

    Using get method"""
    the_user = db.session.get(User, "anonymous")
    the_game = db.session.get(Game, game_id)
    db.session.query(Ownership).filter_by(user=the_user, game=the_game).delete()
    db.session.commit()
    return redirect(url_for("main.index"), code=302)
