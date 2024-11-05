#! /usr/bin/env python3
"""World API back-end

@authors: Roman Yasinovskyy
@version: 2024.11
"""

import csv
from flask import Flask, abort, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)


@app.route("/")
def dummy():
    return jsonify(message="Please go away")


@app.route("/api/<string:country>")
def index(country: str):
    """Return country data as JSON"""
    with open("data/world-countries.csv", "r", encoding="utf-8") as f:
        data = csv.DictReader(f, delimiter=";")
        for row in data:
            if row["name"] == country:
                return row
        else:
            abort(404, "Don't know such country")


@app.errorhandler(404)
def not_found(error):
    """Handle not found errors"""
    ...
    return jsonify(error=str(error)), 404
