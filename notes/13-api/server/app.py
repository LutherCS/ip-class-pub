#!/usr/bin/env python3
"""Fake data API"""

import json
import random

import requests
from faker import Faker
from flask import Flask, Response, jsonify
from flask_cors import cross_origin

app = Flask(__name__)
fake_info = Faker()


@app.route("/api/v1/number")
def send_number():
    """Return a random number"""
    resp = Response(json.dumps({"data": random.randint(1, 100)}))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Content-Type"] = "application/json"
    return resp


@app.route("/api/v1/name")
@cross_origin()
def send_name():
    """Return random name"""

    name = fake_info.name()
    return jsonify(data=name)


@app.route("/api/v1/quote")
@cross_origin()
def send_quote():
    """Return a quote"""
    quotes = requests.get("https://api.quotable.io/quotes/random", timeout=1000).json()
    text = quotes[0].get("content", "Nothing")
    author = quotes[0].get("author", "Nobody")
    return jsonify(data=f"{text} ({author})")


if __name__ == "__main__":
    app.run(debug=True)
