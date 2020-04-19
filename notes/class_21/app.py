"""Requests example"""

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    summary = requests.get("https://api.covid19api.com/summary")
    return render_template("index.html", data=summary.json())


if __name__ == "__main__":
    app.run(host="0.0.0.0")
