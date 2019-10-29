from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
@app.route("/hello/<string:name_param>")
def hello(name_param=None):
    return render_template("index.html", name=name_param)


@app.route("/<int:n>")
def get_numbers(n):
    return render_template("number.html", nums=list(range(n)))
