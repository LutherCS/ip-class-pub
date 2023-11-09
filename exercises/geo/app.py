import requests
from flask import Flask, request, render_template, send_from_directory
from flask import redirect, url_for

app = Flask(__name__)


def get_data_from_db(query: str) -> list:
    """retrieve data from the database and return to the user"""
    raise NotImplementedError


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # display links to 3 options (country / region / continent)
        return render_template("index.html")
    # retrieve data from the database based on the selected option and present it to the user
    raise NotImplementedError


@app.route("/<string:scope>")
def search(scope: str):
    if scope == "country":
        # get countries from the database and populate options of the drop-down menu
        raise NotImplementedError
    elif scope == "region":
        # get regions from the database and populate options of the drop-down menu
        raise NotImplementedError
    elif scope == "continent":
        # get continents from the database and populate options of the drop-down menu
        raise NotImplementedError
