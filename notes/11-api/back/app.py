#! /usr/bin/env python3
"""World API back-end

@authors: Roman Yasinovskyy
@version: 2024.11
"""

from flask import Flask, abort, jsonify

app = Flask(__name__)


@app.route("/api/<string:country>")
def index(country: str):
    """Return country data as JSON"""
    ...


@app.errorhandler(404)
def not_found(error):
    """Handle not found errors"""
    ...
