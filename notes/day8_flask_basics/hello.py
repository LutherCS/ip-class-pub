#!/usr/bin/env python3

from flask import Flask, request

app = Flask(__name__)
from random import choice


@app.route("/")
def hello():
    return "Hello, World"


@app.route("/number/<int:n>")
def is_prime(n):
    return f"{n} {choice(['is', 'is not'])} a prime number"


@app.route("/number/<string:foo>")
def is_not_a_number(foo):
    return f"{foo} is not even a number!"


@app.route("/greet/<string:name>")
def greet_by_name(name):
    return f"Hello, <strong>{name}</strong>"

@app.route("/try")
def hello_form():
    if "firstname" in request.args:
        return greet_by_name(request.args.get('firstname'))
    else:
        return send_form()


def send_form():
    return """
    <form>
        <label for='firstname'>Enter your name</label>
        <input id='firstname' type='text' name='firstname' />
        <input type='submit'>
    </form>
    """
