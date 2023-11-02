#!/usr/bin/en python3
"""Zen of Python API"""

import codecs
import random
import this

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/api/v1/koan")
def send_koan():
    """Return random piece of wisdom"""
    zen = codecs.decode(this.s, "rot13").split("\n")[2:]
    return jsonify(koan=random.choice(zen))


if __name__ == "__main__":
    app.run()
