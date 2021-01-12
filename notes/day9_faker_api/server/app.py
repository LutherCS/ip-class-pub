#!/usr/bin/env python3
"""
Faker API
"""

import json
from flask import Flask, Response, jsonify
from flask_cors import CORS, cross_origin
from faker import Faker

app = Flask(__name__)
# CORS(app)
fake = Faker()


@app.route("/api/v1/name")
def get_name():
    fake_name = fake.name()
    res = Response(json.dumps({"name": fake_name}))
    res.headers["Access-Control-Allow-Origin"] = "*"
    res.headers["Content-Type"] = "application/json"
    return res


@app.route("/api/v1/address")
@cross_origin()
def get_address():
    return jsonify(address=fake.address())


if __name__ == "__main__":
    app.run("0.0.0.0")
