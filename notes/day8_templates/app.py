from flask import Flask, render_template, request, make_response, redirect, url_for

app = Flask(__name__)
import random


def is_prime(n):
    return random.random() < 0.5


def get_n_primes(n):
    all_primes = []
    current_prime_number = 2
    while len(all_primes) < n:
        if is_prime(current_prime_number):
            all_primes.append(current_prime_number)
        current_prime_number = current_prime_number + 1
    return all_primes


@app.route("/")
def index():
    return render_template("index.html", name="CS330")


@app.route("/<int:n>")
def number(n):
    return render_template("primes.html", prime_nums=get_n_primes(n))


@app.route("/game", methods=["GET", "POST"])
def play_game():
    if request.method == "GET":
        a_number = request.cookies.get("number")
        if a_number:
            return render_template("result.html", number=a_number)
        else:
            return render_template("guess.html")
    else:  # POST
        response = make_response(redirect(url_for("play_game"), code=303))
        if request.form.get("done"):
            response.set_cookie("number", "", expires=0)
        else:
            response.set_cookie("number", request.form.get("number"))
        return response
