#!/usr/bin/env python3

"""
Simple CORS proxy

@author: Roman Yasinovskyy
@version: 2025.10
"""

import requests
from flask import Flask, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.get("/api/fruit/<string:name>")
def proxy(name: str):
    base_url = "https://www.fruityvice.com/api/fruit"
    return json.loads(requests.get(f"{base_url}/{name}").content)


if __name__ == "__main__":
    app.run()
