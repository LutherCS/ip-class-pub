#!/usr/bin/env python3
"""
Board Game Record Keeper

@author: Roman
@version: 2022.10
"""

from csv import DictReader
from flask import (
    Flask,
    make_response,
    redirect,
    render_template,
    request,
    url_for,
    jsonify,
)

app = Flask(__name__)

all_games = dict()
chosen_games = dict()


@app.get("/")
def index():
    global all_games
    global chosen_games
    if not all_games:
        with open("data/games.csv") as datafile:
            for record in DictReader(datafile):
                all_games[record["title"]] = record
    if not chosen_games:
        return render_template("base.html", games=all_games.values())
    return render_template(
        "games.html", games=all_games.values(), collection=chosen_games.values()
    )


@app.post("/addgame")
def read_user_selection():
    global all_games
    global chosen_games
    response = make_response(redirect(url_for("index"), code=303))
    game_title = request.form.get("game")
    chosen_games[game_title] = all_games[game_title]

    return response


@app.get("/api/v1/games/all")
def get_all_games():
    global all_games
    return jsonify(all_games)


@app.get("/api/v1/games/my")
def get_user_games():
    global chosen_games
    return jsonify(chosen_games)
