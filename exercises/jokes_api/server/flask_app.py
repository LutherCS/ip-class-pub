from flask import Flask, Response, jsonify
from flask_cors import cross_origin, CORS
import json
import pyjokes

app = Flask(__name__)
CORS(app)

@app.route('/api/v1/jokes')
#@cross_origin()
def get_random_joke():
    joke = pyjokes.get_joke(language='en', category='all')
    resp = Response(json.dumps({"joke": joke}))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Content-Type"] = "application/json"

    return resp

@app.route('/api/v1/jokes/<joke_id>', methods=['GET'])
#@cross_origin()
def get_specific_joke():
    joke_list = pyjokes.get_jokes(language='en', category='all')
    joke = joke_list[joke_id]
    resp = Response(json.dumps({"joke": joke}))
    resp.headers["Access-Control-Allow-Origin"] = "*"
    resp.headers["Content-Type"] = "application/json"


    return resp

