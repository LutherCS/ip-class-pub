"""
GamelYY

@author: Roman Yasinovskyy
@version: 2026.10
"""

import csv

from flask import Flask


def create_app() -> Flask:
    from gamelyy.model import Library
    from gamelyy.routes import main

    this_app = Flask(__name__)
    this_app.config["SHELF"] = Library()
    with open("dataset.csv") as datasource:
        this_app.config["DB"] = list(csv.DictReader(datasource))

    this_app.register_blueprint(main)
    return this_app
