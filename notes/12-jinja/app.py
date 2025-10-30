#!/usr/bin/env python3

"""
Fruittime with Jinja templates

@author: CS330
@version: 2025.10
"""

import requests
from flask import (
    Flask,
    abort,
    json,
    redirect,
    render_template,
    request,
    send_from_directory,
    url_for,
)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

RATINGS = {4: "Excellent", 3: "Good", 2: "Regular", 1: "Bad"}
REVIEWS = []
COLORS = {1: "danger", 2: "warning", 3: "info", 4: "success"}


@app.get("/")
def index():
    return render_template("reviews.jinja", reviews=REVIEWS, ratings=RATINGS, colors=COLORS)


@app.post("/")
def save_review():
    fruit_name = request.form.get("fruit_name")
    fruit_rating = int(request.form.get("fruit_rating"))
    fruit_opinion = request.form.get("fruit_opinion")
    REVIEWS.append({"name": fruit_name, "rating": fruit_rating, "opinion": fruit_opinion})
    return render_template("reviews.jinja", reviews=REVIEWS, ratings=RATINGS, colors=COLORS)


@app.get("/api/fruit/<string:name>")
def proxy(name: str):
    base_url = "https://www.fruityvice.com/api/fruit"
    return json.loads(requests.get(f"{base_url}/{name}").content)


if __name__ == "__main__":
    app.run()
