#!/usr/bin/env python3
"""Flask demo"""

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello, CS330 students"


@app.route("/<name>")
def greet(name: str):
    return f"Hello, {name}"


@app.route("/<int:number>")
def number_counter(number: int):
    return "<p>Hello, <strong>student</strong></p>" * number


@app.route("/<string:name>/<int:number>")
def greet_by_name(name: str, number: int):
    return f"<p>Hello, <strong>{name}</strong></p>" * number


@app.get("/hello")
def greet_by_first_name():
    if "firstname" in request.args:
        return greet(request.args.get("firstname"))
    return send_form()


@app.get("/bye")
def parting_by_first_name():
    if "firstname" in request.args:
        return greet(request.args.get("firstname"))
    return send_form(method="post")


@app.post("/bye")
def parting_by_name_post():
    if "firstname" in request.form:
        return greet(request.form.get("firstname"))


def send_form(method: str = "get") -> str:
    return f"""
<form method="{method}">
<input id="firstname" type="text" placeholder="First name" name="firstname">
<input type="submit" value="Submit">
</form>
"""


if __name__ == "__main__":
    app.run(debug=True)
