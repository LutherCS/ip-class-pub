#!/usr/bin/env python3

import records
from flask import Flask, request, render_template

app = Flask(__name__)

THE_WORLD = []
CACHE = {}

def get_data(host: str, port: int, user: str, dbname: str, query: str) -> list:
    db = records.Database(f"postgres://{user}:@{host}:{port}/{dbname}")
    rows = db.query(query)
    return rows


@app.route("/", methods=["GET", "POST"])
def index():
    global CACHE

    if request.method == "GET":
        return render_template("index.html")
    if request.form.get("country"):
        country = request.form.get("country")
        if country in CACHE:
            result = CACHE[country]
        else:
            result = get_data(
                host="localhost",
                port=2345,
                user="yasiro01",
                dbname="world",
                query=f"select * from country where code = '{country}';",
            )
            CACHE[country] = result
        return render_template("result.html", rows=result)


@app.route("/country")
def country():
    global THE_WORLD
    if not THE_WORLD:
        THE_WORLD = get_data(
            host="localhost",
            port=2345,
            user="yasiro01",
            dbname="world",
            query="select code, name from country;",
        )
    return render_template("country.html", options=THE_WORLD)


if __name__ == "__main__":
    app.run()
