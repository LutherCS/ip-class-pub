from flask import Flask

app = Flask(__name__)


@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello, CS330!"
