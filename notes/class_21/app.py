"""Requests example"""

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    pass


if __name__ == "__main__":
    app.run(host="0.0.0.0")
