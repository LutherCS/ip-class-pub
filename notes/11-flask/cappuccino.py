"""Sample Flask app"""
import sys

from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Your cappuccino is here!"


@app.route("/<drink_name>")
def drink(drink_name):
    return f"Would you like some {drink_name}?"


@app.route("/<int:n>")
def many_drinks(n):
    return f"Would you like {n} cappuccinos?"


@app.route("/q/<path:subpath>")
def drink_and_num(subpath):
    try:
        drink, number = subpath.split("/")
        return f"Would you like {number} cups of {drink}?"
    except ValueError as v_err:
        print(v_err, file=sys.stderr)
        return "Would you like a cup of cappuccino?"


@app.route("/order")
def order_drink():
    if "drink" in request.args:
        drink = request.args.get("drink")
        if not drink:
            drink = "cappuccino"
        return f"Would you like some {drink}?"
    return send_form()


def send_form():
    return """
        <form>
          <label for='drink'>What would you like to drink?</label>
          <input type='text' name='drink' />
          <input type='submit' value='Order' />
        </form>
            """


if __name__ == "__main__":
    app.run()
