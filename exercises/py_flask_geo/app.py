import requests
from flask import Flask, request, render_template, send_from_directory
from flask import redirect, url_for
import records

app = Flask(__name__)


USER = ""
DB_NAME = "world"
HOST = "localhost"
PORT = 2345


def get_data_from_db(query: str) -> list:
    db = records.Database(f"postgresql://{USER}:@{HOST}:{PORT}/{DB_NAME}")
    # retrieve data from the database and return to the user
    pass


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # display links to 3 options (country / region / continent)
        pass
    else:
        # retrieve data from the database based on the selected option and present it to the user
        pass


@app.route("/<string:scope>", methods=["GET"])
def search(scope: str):
    if scope == "country":
        # get countries from the database and populate options of the drop-down menu
        pass
    elif scope == "region":
        # get regions from the database and populate options of the drop-down menu
        pass
    elif scope == "continent":
        # get continents from the database and populate options of the drop-down menu
        pass
