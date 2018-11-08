import os
import requests
from flask import Flask, request, render_template, send_from_directory
from flask import redirect, url_for
import psycopg2
import records

app = Flask(__name__)


def get_data_from_db(query: str) -> list:
    raise NotImplementedError


@app.route("/", methods=["GET", "POST"])
def index():
    raise NotImplementedError


@app.route("/country", methods=["GET"])
def country():
    raise NotImplementedError


if __name__ == "__main__":
    app.run(host="0.0.0.0")
