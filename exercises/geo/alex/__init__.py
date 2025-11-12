#!/usr/bin/env python3
"""
Geography app initialization

@author: Roman Yasinovskyy
@version: 2025.11
"""

import pathlib

from dotenv import load_dotenv
from flask import Flask


def create_app():
    """Create Flask app"""
    from .routes import main
    from .retrieval import get_data_from_db

    app = Flask(__name__)
    # Load configuration
    if pathlib.Path(".flaskenv").exists():
        load_dotenv(".flaskenv")
    else:
        load_dotenv("exercises/geo/.flaskenv")
    app.config.from_prefixed_env()
    # Specify the database location
    if __name__ == "alex":
        db_dir = "data"
    else:
        db_dir = "exercises/geo/data"
    data_source = pathlib.Path(pathlib.Path(db_dir) / pathlib.Path(app.config["DB_FILE"]))
    if not data_source.exists():
        raise FileNotFoundError("Database not found")
    app.config["DB_FILE"] = data_source
    # Register routes
    app.register_blueprint(main)
    # Populate regions, subregions, and countries as part of the app config
    # TODO: Populate app.config["regions"] with all the distinct regions for later use in templates
    # TODO: Populate app.config["subregions"] with all the distinct subregions for later use in templates
    # TODO: Populate app.config["countries"] with all the distinct countries for later use in templates
    return app
