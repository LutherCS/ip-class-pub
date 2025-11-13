#!/usr/bin/env python3
"""
Flask to CRUD

@author:
@version: 2025.11
"""

import logging
import pathlib
from functools import cache

from crud_sqlite import create, delete, read, update
from flask import Flask, jsonify, redirect, url_for

filename = "orchard"


def create_app():
    app = Flask(__name__)
    if not pathlib.Path(f"{filename}.db").exists():
        create.callback(f"{filename}.db", f"{filename}.csv")
    else:
        logging.warning("Database already exists")

    return app


app = create_app()


@cache
@app.get("/")
def read_all():
    data = read.callback(f"{filename}.db")
    return jsonify(data)


@cache
@app.get("/<int:fruit_id>")
def read_one(fruit_id: int):
    data = read.callback(f"{filename}.db", fruit_id)
    return jsonify(data)


@app.post("/")
def update_all():
    update.callback(f"{filename}.db")
    return redirect(url_for("read_all"))


@app.post("/<int:fruit_id>")
def update_one(fruit_id: int):
    update.callback(f"{filename}.db", fruit_id)
    return redirect(url_for("read_one", fruit_id=fruit_id))


@app.delete("/")
def delete_all():
    delete.callback(f"{filename}.db")
    return redirect(url_for("read_all"))


@app.delete("/<int:fruit_id>")
def delete_one(fruit_id: int):
    delete.callback(f"{filename}.db", fruit_id)
    return redirect(url_for("read_one", fruit_id=fruit_id))
