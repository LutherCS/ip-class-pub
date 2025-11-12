#!/usr/bin/env python3
"""
Geography app routes

@author:
@version: 2025.11
"""

from flask import Blueprint, abort, current_app, flash, redirect, render_template, request, url_for
from werkzeug.wrappers import Response

from .retrieval import get_data_from_db

main = Blueprint("main", __name__, url_prefix="/")


@main.route("/")
def world() -> str:
    """Display default page"""
    # TODO: Implement this function
    ...


@main.get("/region", defaults={"name": None})
@main.get("/region/<string:name>")
def region(name: str | None) -> str | Response:
    """Display region information"""
    # TODO: Implement this function
    ...


@main.get("/subregion", defaults={"name": None})
@main.get("/subregion/<string:name>")
def subregion(name: str | None) -> str | Response:
    """Display subregion information"""
    # TODO: Implement this function
    ...


@main.get("/country", defaults={"name": None})
@main.get("/country/<string:name>")
def country(name: str | None) -> str | Response:
    """Display country information"""
    # TODO: Implement this function
    ...


@main.errorhandler(404)
def not_found(err):
    # TODO: Implement this function
    ...
    flash(err, "warning")
