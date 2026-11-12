"""
GamelYY

@author: Roman Yasinovskyy
@version: 2026.10
"""

import csv
import pathlib

import dotenv
from flask import Flask


def create_app() -> Flask:
    from gamelyy.logic import close_db
    from gamelyy.routes import main

    this_dir = pathlib.Path(__file__).parent
    this_app = Flask(__name__)
    this_app.teardown_appcontext(close_db)
    dotenv.load_dotenv(this_dir / pathlib.Path(".flaskenv"))
    this_app.config.from_prefixed_env()
    this_app.config["user"] = "anonymous"

    if pathlib.Path(this_dir / pathlib.Path(this_app.config["DATABASE"])).exists():
        raise FileNotFoundError("Database not found")

    this_app.register_blueprint(main)
    return this_app
