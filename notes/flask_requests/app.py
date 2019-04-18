from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def blog():
    posts_response = requests.get("http://jsonplaceholder.typicode.com/posts")
    users_response = requests.get("http://jsonplaceholder.typicode.com/users")
    comments_response = requests.get("http://jsonplaceholder.typicode.com/comments")
    return render_template(
        "index.html",
        posts=posts_response.json(),
        users=users_response.json(),
        comments=comments_response.json(),
    )
