"""
GamelYY

@author: Roman Yasinovskyy
@version: 2026.11
"""

import pathlib

import dotenv
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
mm = Marshmallow()


def create_app() -> Flask:
    from gamelyy.model import add_anonymous_user, load_data
    from gamelyy.routes import main

    this_app = Flask(__name__)
    app_dir = pathlib.Path(__file__).parents[1]
    dotenv.load_dotenv(app_dir / pathlib.Path(".flaskenv"))
    this_app.config.from_prefixed_env()
    db_file = app_dir / pathlib.Path(f"{this_app.config['DATA_FILE']}.sqlite3")
    this_app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_file}"
    db.init_app(this_app)
    if not pathlib.Path(this_app.config["SQLALCHEMY_DATABASE_URI"]).exists():
        with this_app.app_context():
            db.create_all()
            load_data(f"{this_app.config['DATA_FILE']}.csv")
            add_anonymous_user()
    this_app.register_blueprint(main)
    return this_app
