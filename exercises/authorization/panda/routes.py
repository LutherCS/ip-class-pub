#!/usr/bin/env python3
"""
PandAuth routes

@author: Roman Yasinovskyy
@version: 2025.12
"""

from flask import Blueprint, render_template

main = Blueprint("main", __name__, url_prefix="/")


@main.route("/")
def index():
    return render_template("index.jinja")
