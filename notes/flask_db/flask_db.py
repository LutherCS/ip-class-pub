import os
import requests
from flask import Flask, request, render_template, send_from_directory
from flask import redirect, url_for
import psycopg2
import records

app = Flask(__name__)


def get_data_from_db(query: str) -> list:
    pass


@app.route("/", methods=["GET", "POST"])
def index():
    pass


@app.route("/country", methods=["GET"])
def country():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0")
