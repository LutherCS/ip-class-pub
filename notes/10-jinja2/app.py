#!/usr/env/bin python3

import random
from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)


@app.route("/")
def index():
    return render_template(
        "index.html",
    )


# @app.route("/game", methods=["GET", "POST"])
# def game():
#     if request.method == "GET":
#         ...
#     else:
#         ...


@app.get("/game")
def get_game_form():
    number = request.cookies.get("guess", None)
    if number:
        return render_template("result.html", number=int(number), correct=308)
    return render_template("guess_form.html", numbers=random.sample(range(1, 100), 10))


@app.post("/game")
def post_game_form():
    response = make_response(redirect(url_for("get_game_form"), code=303))
    if request.form.get("again"):
        response.set_cookie("guess", "", expires=0)
    else:
        number = request.form.get("number")
        response.set_cookie("guess", number)
    return response


@app.errorhandler(404)
def not_found(error):
    return render_template("error404.html", message=error)


if __name__ == "__main__":
    app.run()
