import os
import requests
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def hello_user():
    flask_posts = requests.get('http://jsonplaceholder.typicode.com/posts')
    flask_users = requests.get('http://jsonplaceholder.typicode.com/users')
    return render_template("index.html", posts=flask_posts.json(), users=flask_users.json())


# @app.route('/js/<path:filename>')
# def serve_static(filename):
#     root_dir = os.path.dirname(os.getcwd())
#     return send_from_directory(os.path.join(root_dir, 'static', 'js'), filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
