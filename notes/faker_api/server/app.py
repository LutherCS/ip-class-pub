from flask import Flask, Response, jsonify
from flask_cors import cross_origin
import json
from faker import Faker

app = Flask(__name__)
fake = Faker()


@app.route("/api/v1/names")
def get_name():
    resp = Response(json.dumps({"name": fake.name()}))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Content-Type"] = "application/json"
    return resp


@app.route("/api/v1/addresses")
@cross_origin()
def get_address():
    return jsonify(address=fake.address())


@app.route("/api/v1/sentences")
@cross_origin()
def get_sentence():
    return jsonify(sentence=fake.sentence())
