#!/usr/bin/env python3
"""
Movie mash

@author: Roamn Yasinovskyy
@version: 2024.11
"""

import psycopg

from flask import Flask, flash, render_template, request
from psycopg.rows import dict_row
from werkzeug.wrappers import Response


def create_app():
    my_app = Flask(__name__)
    my_app.config.from_prefixed_env()
    return my_app


app = create_app()


@app.route("/")
def index() -> str:
    """Display default page"""
    return render_template("index.html")


@app.post("/")
def post_names() -> str | Response:
    """Display movie information"""
    query = """
with list1 as
(select *
from moviecast
where name=%s),
list2 as
(select *
from moviecast
where name=%s)
select * from
list1 inner join list2
on list1.title=list2.title
"""
    name1 = request.form.get("name1")
    name2 = request.form.get("name2")
    try:
        with psycopg.connect(app.config["DB_URI"]) as conn:
            result = (
                conn.cursor(row_factory=dict_row)
                .execute(query, (name1, name2))
                .fetchall()
            )
    except psycopg.OperationalError as op_err:
        print(op_err)
    if not result:
        flash(f"There is not match between {name1} and {name2}")
    return render_template("index.html", data=result)


if __name__ == "__main__":
    app.run()
