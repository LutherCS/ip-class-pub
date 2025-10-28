#!/usr/bin/env python3

"""
Flask intro

@author: Roman Yasinovskyy
@version: 2025.10
"""

import requests
from flask import Flask, json, send_from_directory, abort
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

fruits = ["Apple", "Avocado", "Blueberry", "Cherry"]


@app.route("/")
def get_flask_time() -> str:
    # return f"The time is {datetime.now()}"
    result = ""
    for fruit in fruits:
        result += f"<a href='http://localhost:5000/{fruit}'>{fruit}</a><br>"
    return result


@app.route("/<int:idx>")
def fruit_by_id(idx: int) -> str:
    try:
        return fruits[idx]
    except IndexError:
        abort(404, f"Unknown fruit number: {idx}")


@app.route("/<string:name>")
def fruit_by_name(name: str) -> str:
    if name.capitalize() in fruits:
        return f"We do have information about <strong>{name}</strong> in our database"
    abort(404, f"Unknown fruit name: {name}")


@app.route("/app/<string:filename>")
def send_file(filename):
    return send_from_directory("static", path=filename)


@app.get("/api/fruit/<string:name>")
def proxy(name: str):
    base_url = "https://www.fruityvice.com/api/fruit"
    return json.loads(requests.get(f"{base_url}/{name}").content)


@app.errorhandler(404)
def not_found(error: str) -> tuple[str, int]:
    return f"<strong>{error}</strong>", 404


if __name__ == "__main__":
    app.run()
