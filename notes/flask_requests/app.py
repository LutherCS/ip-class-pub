#!/usr/bin/env python3

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    posts = requests.get("http://jsonplaceholder.typicode.com/posts")
    users = requests.get("http://jsonplaceholder.typicode.com/users")
    comms = requests.get("http://jsonplaceholder.typicode.com/comments")
    return render_template(
        "index.html",
        jj_posts=posts.json(),
        jj_users=users.json(),
        jj_comms=comms.json(),
    )
