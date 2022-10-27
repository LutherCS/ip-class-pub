#!/usr/bin/env python3
"""
Board Game Record Keeper

@author: Roman
@version: 2022.10
"""

from flask import Flask, render_template, request
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, <strong>student</strong>!"


@app.route("/<string:name>")
def greet_by_name(name: str):
    return render_template("hello.html", name=name)


@app.route("/<string:name>/<int:times>")
def greet_many_times(name: str, times: int) -> str:
    return render_template("hello.html", names=[name] * times)


@app.route("/sum/<path:subpath>")
def sum_of_2(subpath):
    a, b = subpath.split("/")
    return f"The sum of {a} and {b} is {do_stuff(int(a), int(b))}"


@app.route("/mult/<int:a>/<int:b>")
@app.route("/prod/<int:a>/<int:b>")
def prod_of_2(a: int, b: int) -> str:
    return f"The product of {a} and {b} is {a * b}"


def do_stuff(a: int, b: int) -> int:
    return a + b


@app.route("/math")
def do_math() -> str:
    if not request.args:
        return """
<form>
<select name="a">
    <option value="1">1</option>
    <option value="2">2</option>
    <option value="3">3</option>
</select>
<select name="b">
    <option value="1">1</option>
    <option value="5">5</option>
    <option value="10">10</option>
</select>
<select name="op">
    <option value="+">+</option>
    <option value="*">*</option>
</select>
<input type='submit'>
</form>
"""
    else:
        if request.args.get("op") == "+":
            return sum_of_2(f"{request.args.get('a')}/{request.args.get('b')}")
        if request.args.get("op") == "*":
            return prod_of_2(int(request.args.get("a")), int(request.args.get("b")))
