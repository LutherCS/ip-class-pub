#!/usr/bin/env python3

"""
Fruittime initialization

@author: CS330
@version: 2025.11
"""

import pathlib

import dotenv
from flask import Flask
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
login_manager.login_view = "auth.login"
db = SQLAlchemy()
mm = Marshmallow()


def create_app() -> Flask:
    from fruittime.routes import main
    from fruittime.auth import auth

    this_app = Flask(__name__)
    this_dir = pathlib.Path(__file__).parent
    dotenv.load_dotenv(this_dir / pathlib.Path(".flaskenv"))
    this_app.config.from_prefixed_env()
    db_file = this_dir.parent / pathlib.Path(f"{this_app.config['DATA_FILE']}.sqlite3")
    this_app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:////{db_file}"
    this_app.config["RATINGS"] = {4: "Excellent", 3: "Good", 2: "Regular", 1: "Bad"}
    this_app.config["COLORS"] = {1: "danger", 2: "warning", 3: "info", 4: "success"}
    login_manager.init_app(this_app)
    db.init_app(this_app)
    with this_app.app_context():
        db.create_all()
    with this_app.app_context():
        mm.init_app(this_app)
    this_app.register_blueprint(main)
    this_app.register_blueprint(auth)

    return this_app
