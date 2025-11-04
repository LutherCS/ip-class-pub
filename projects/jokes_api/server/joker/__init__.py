#!/usr/bin/env python3
"""
jokes api

@author:
@version: 2025.11
"""

import pathlib
import tomllib

from flask import Flask
from flask_cors import CORS

from .logic import Joker


def create_app() -> Flask:
    this_app = Flask(__name__)

    # TODO: Implement this function

    return this_app
