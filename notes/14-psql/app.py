#!/usr/bin/env python3
"""
Movie mash

@author: Roamn Yasinovskyy
@version: 2024.11
"""

import psycopg

from flask import Flask, render_template, request
from psycopg.rows import dict_row
from werkzeug.wrappers import Response


app = Flask(__name__)


@app.route("/")
def index() -> str:
    """Display default page"""
    return render_template("index.html")


@app.post("/")
def post_names() -> str | Response:
    """Display movie information"""
    query = ""
    name1 = request.form.get("name1")
    name2 = request.form.get("name2")
    try:
        with psycopg.connect(
            "postgresql://yasiro01:@knuth.luther.edu:5432/movies"
        ) as conn:
            result = (
                conn.cursor(row_factory=dict_row)
                .execute(query, (name1, name2))
                .fetchall()
            )
    except psycopg.OperationalError as op_err:
        pass
    return render_template("index.html", data=result)


if __name__ == "__main__":
    app.run()
