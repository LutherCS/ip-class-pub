from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    else:
        country_code = request.form.get("country")
        country_info = get_data_from_db(f"select * from country where code='{country_code}'")
        return render_template("result.html", rows=country_info)


@app.route("/country")
def country():
    all_countries = get_data_from_db("select code, name from country;")
    return render_template("country.html", options=all_countries)


def get_data_from_db(stmt):
    try:
        conn = psycopg2.connect(
            user="yasiro01", host="knuth.luther.edu", port=5432, dbname="world"
        )
    except:
        raise ConnectionError("could not connect to the database")
    cur = conn.cursor()
    cur.execute(stmt)
    rows = cur.fetchall()
    return rows
