#!/usr/bin/env python3
import random
import pyjokes
from flask import Flask, request, render_template, url_for, make_response

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    pass

def send_joke(category: str, language: str, number: int):
    pass
