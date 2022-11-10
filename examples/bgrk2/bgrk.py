#!/usr/bin/env python3
"""
Board Game Record Keeper

@author: Roman
@version: 2022.11
"""

from csv import DictReader
from functools import cache
from os import environ

import requests
from dotenv import load_dotenv
from flask import (
    Flask,
    jsonify,
    make_response,
    redirect,
    render_template,
    request,
    session,
    url_for,
)


@cache
def read_data_file(filename):
    all_games = {}
    with open(filename) as datafile:
        for record in DictReader(datafile):
            all_games[record["title"]] = record
    return all_games


def create_app():
    app = Flask(__name__)
    load_dotenv()
    app.config.from_prefixed_env()
    app.config["all_games"] = read_data_file("data/games.csv")
    app.config["bga_client_id"] = environ["BGA_CLIENT_ID"]

    return app


app = create_app()


@app.get("/")
def index():
    all_games = app.config["all_games"]
    chosen_games = session.get("chosen_games", [])
    if not chosen_games:
        return render_template("base.html", games=all_games.values())
    return render_template(
        "games.html", games=all_games.values(), collection=chosen_games
    )


@app.post("/addgame")
def read_user_selection():
    all_games = app.config["all_games"]
    response = make_response(redirect(url_for("index"), code=303))
    game_title = request.form.get("game")
    game_info_bga = requests.get(
        f"https://api.boardgameatlas.com/api/search?name={game_title}&client_id={app.config['bga_client_id']}"
    )
    game_min_age = 0
    try:
        game_min_age = game_info_bga.json()["games"][0]["min_age"]
    except Exception:
        pass
    chosen_games = session.get("chosen_games", [])
    new_game = all_games[game_title]
    new_game["min_age"] = game_min_age
    chosen_games.append(new_game)
    session["chosen_games"] = chosen_games

    return response


@app.get("/api/v1/games/all")
def get_all_games():
    all_games = app.config["all_games"]
    return all_games


@app.get("/api/v1/games/my")
def get_user_games():
    chosen_games = session.get("chosen_games", [])
    return jsonify(chosen_games)
