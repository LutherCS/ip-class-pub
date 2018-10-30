from flask import Flask
from flask import request
from flask import render_template
from flask import url_for
from flask import redirect
from flask import make_response
from flask import Response
from flask import jsonify

import json


app = Flask(__name__)

@app.route('/add')
def adder():
    n1 = request.args.get('num1')
    n2 = request.args.get('num2')
    response  = Response(json.dumps({'result': int(n1) + int(n2)}))
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':
    app.run()
