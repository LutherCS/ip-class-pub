import os
import requests
from flask import Flask, request, render_template, send_from_directory
from flask import redirect, url_for
import psycopg2
import records

app = Flask(__name__)


def get_data_from_db(query: str) -> list:
    try:
        conn = psycopg2.connect(user="yasiro01", host="knuth.luther.edu", port=5432, dbname="world")
    except:
        raise ConnectionError("Bad stuff")
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    if request.form.get("country"):
        country_code = request.form.get("country")
        query = f"select * from country where code='{country_code}'"
        result = get_data_from_db(query)
        print(result)
        return render_template("result.html", rows=result)


@app.route("/country", methods=["GET"])
def country():
    all_countries = get_data_from_db("select code, name from country;")
    return render_template("country.html", options=all_countries)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
