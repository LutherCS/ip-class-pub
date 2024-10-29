#!/usr/bin/env python3
"""
Serving `pyjokes` via templates

@authors:
@version: 2024.10
"""

import random

import pyjokes
from flask import Flask, abort, render_template, request
from pyjokes.exc import PyjokesError

LANGUAGES = {
    "cs": "CZECH",
    "de": "GERMAN",
    "en": "ENGLISH",
    "es": "SPANISH",
    "eu": "BASQUE",
    "fr": "FRENCH",
    "gl": "GALICIAN",
    "hu": "HUNGARIAN",
    "it": "ITALIAN",
    "lt": "LITHUANIAN",
    "pl": "POLISH",
    "sv": "SWEDISH",
}

app = Flask(__name__)


@app.get("/")
def index():
    """Render the template with form"""
    # TODO: Implement this function
    ...


@app.post("/")
def index_jokes():
    """Render the template with jokes"""
    # TODO: Implement this function
    ...


def get_jokes(
    language: str = "en",
    category: str = "all",
    number: int = 1,
) -> list[str]:
    """Return a list of jokes"""
    # TODO: Implement this function
    ...
