#!/usr/bin/env python3

"""
Fruittime logic

@author: CS330
@version: 2025.11
"""

import requests
import json


def get_data(name: str):
    base_url = "https://www.fruityvice.com/api/fruit"
    return json.loads(requests.get(f"{base_url}/{name}").content)
