from flask import Flask
from flask import request
from flask import Response

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
