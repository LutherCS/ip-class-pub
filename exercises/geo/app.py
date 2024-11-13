#!/usr/bin/env python3
"""
Geography query app

@authors:
@version: 2024.11
"""

import pathlib
import sqlite3

from dotenv import load_dotenv
from flask import Flask, abort, flash, redirect, render_template, request, url_for
from werkzeug.wrappers import Response


def create_app():
    """Create Flask app"""
    this_app = Flask(__name__)
    if pathlib.Path(".flaskenv").exists():
        this_app.config.from_prefixed_env()
    else:
        load_dotenv("exercises/geo/.flaskenv")
        this_app.config.from_prefixed_env()
    return this_app


app = create_app()


def get_data_from_db(query: str, params: tuple | None = None) -> list:
    """Retrieve data from the database

    :param query: parametrized query to execute
    :param params: query parameters
    """
    # TODO: Implement this function
    ...


@app.route("/")
def index() -> str:
    """Display default page"""
    return render_template("index.html")


@app.get("/country")
def country_form() -> str | Response:
    """Display country search form"""
    # TODO: Implement this function
    ...


@app.get("/country/<string:name>")
def country_info(name: str) -> str:
    """Display country information"""
    # TODO: Implement this function
    ...


@app.get("/region")
def region_form() -> str | Response:
    """Display region search form"""
    # TODO: Implement this function
    ...


@app.get("/region/<string:name>")
def region_info(name: str) -> str:
    """Display region information"""
    # TODO: Implement this function
    ...


@app.get("/subregion")
def subregion_form() -> str | Response:
    """Display subregion search form"""
    # TODO: Implement this function
    ...


@app.get("/subregion/<string:name>")
def subregion_info(name: str) -> str:
    """Display subregion information"""
    # TODO: Implement this function
    ...


@app.errorhandler(404)
def not_found(err):
    # TODO: Implement this function
    ...


if __name__ == "__main__":
    app.run()
