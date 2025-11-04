#!/usr/bin/env python3

"""
Fruittime initialization

@author: CS330
@version: 2025.11
"""

import pathlib
import dotenv
from flask import Flask
from flask_cors import CORS


def create_app() -> Flask:
    from fruittime.routes import main
    from .models import Reviews

    this_app = Flask(__name__)
    CORS(this_app)
    this_dir = pathlib.Path(__file__).parent
    dotenv.load_dotenv(this_dir / pathlib.Path(".flaskenv"))
    this_app.config.from_prefixed_env()
    this_app.config["RATINGS"] = {4: "Excellent", 3: "Good", 2: "Regular", 1: "Bad"}
    this_app.config["COLORS"] = {1: "danger", 2: "warning", 3: "info", 4: "success"}
    this_app.config["REVIEWS"] = Reviews()

    this_app.register_blueprint(main)
    return this_app
