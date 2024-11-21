#!/usr/bin/env python3
"""App config file"""

import pathlib

from dotenv import load_dotenv
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


def create_app():
    """Create Flask app"""
    this_app = Flask(__name__)
    this_dir = pathlib.Path(__file__).parent
    load_dotenv(this_dir / pathlib.Path(".flaskenv"))
    this_app.config.from_prefixed_env()
    db_file = this_dir / pathlib.Path(f"{this_app.config["DATABASE_FILE"]}.sqlite3")
    this_app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:////{db_file}"
    return this_app


# App object
app = create_app()
# Database object
db = SQLAlchemy(app)
# Marshmallow object
mm = Marshmallow(app)
