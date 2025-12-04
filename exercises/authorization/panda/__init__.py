#!/usr/bin/env python3
"""
PandAuth initialization

@author: Roman Yasinovskyy
@version: 2025.12
"""

import pathlib
import secrets

import dotenv
import requests
from flask import Flask
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from oauthlib.oauth2 import WebApplicationClient


login_manager = LoginManager()
login_manager.login_view = "auth.login"
db = SQLAlchemy()
mm = Marshmallow()
client = WebApplicationClient("")


def create_app() -> Flask:
    from .auth import auth
    from .routes import main

    app = Flask(__name__)

    # Load configuration
    app_dir = pathlib.Path(__file__).parents[1]
    dotenv.load_dotenv(app_dir / pathlib.Path(".flaskenv"))
    app.config.from_prefixed_env()
    app.config.from_mapping(dotenv.dotenv_values(app_dir / pathlib.Path(".env")))

    # Initialize secret key if necessary
    if not app.config.get("SECRET_KEY"):
        app.config["SECRET_KEY"] = secrets.token_hex()

    # Initialize login subsystem
    login_manager.init_app(app)
    with app.app_context():
        client.client_id = app.config["GOOGLE_CLIENT_ID"]
    GOOGLE_DISCOVERY_URL = "https://accounts.google.com/.well-known/openid-configuration"
    app.config["GOOGLE_CONFIG"] = requests.get(GOOGLE_DISCOVERY_URL).json()

    # Initialize database
    db_file = app_dir / pathlib.Path(f"{app.config['DATABASE']}")
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:////{db_file}"
    db.init_app(app)
    if not pathlib.Path(app.config["SQLALCHEMY_DATABASE_URI"]).exists():
        with app.app_context():
            db.create_all()
    with app.app_context():
        mm.init_app(app)

    # Register routes
    app.register_blueprint(main)
    app.register_blueprint(auth)

    return app
