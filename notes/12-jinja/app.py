import random
from flask import Flask, render_template, make_response, request, redirect

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html", name="CS330")


@app.route("/user/<uname>")
def greet_by_name(uname):
    return render_template("index.html", name=uname)


@app.route("/<int:number>")
def get_prime_numbers(number):
    return render_template("primes.html", numbers=get_n_primes(number))


def get_n_primes(n):
    all_primes = []
    current_number = 2
    while len(all_primes) < n:
        if is_prime(current_number):
            all_primes.append(current_number)
        current_number += 1
    return all_primes


def is_prime(number):
    """Is it a prime number?"""
    return random.random() < 0.5


@app.get("/game")
def play_game_get():
    number = request.cookies.get("number")
    if number:
        return render_template("result.html", number=number)
    return render_template("guess.html", numbers=[1, 2, 3])


@app.post("/game")
def play_game_post():
    response = make_response(redirect("/game", code=303))
    if request.form.get("playagain"):
        response.set_cookie("number", "", expires=0)
    else:
        response.set_cookie("number", request.form.get("number"))
    return response
