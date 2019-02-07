from flask import Flask
from flask import redirect, url_for
from flask import request, make_response
from flask import render_template
import math

app = Flask(__name__)


def is_prime(n: int) -> bool:
    raise NotImplementedError


def get_n_primes(n: int) -> list:
    raise NotImplementedError


@app.route('/')
def index():
    raise NotImplementedError

@app.route('/<int:n>')
def get_primes(n):
    raise NotImplementedError

@app.route('/ask')
def ask_a_number():
    raise NotImplementedError


if __name__ == '__main__':
    app.run()
