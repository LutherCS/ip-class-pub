from flask import Flask, request
import random

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, CS330!'

@app.route('/random/<int:n>')
def get_number(n):
    return str(random.randint(0, n))

@app.route('/random/<string:name>')
def get_name(name):
    roster = {"Alice": "Aardvark", "Bob": "Beaver"}
    return roster.get(name, "Human")

@app.route("/path/<path:subpath>")
def print_subpath(subpath):
    return subpath


@app.route("/hello", methods=['GET', 'POST'])
def greet_user():
    if request.method == "POST":
        return "You posted something"
    if 'username' in request.args:
        print(list(request.args.keys()))
        return hello(request.args['username'])
    else:
        return send_form()

def hello(name):
    return f"Hello, <strong>{name}</strong>"


def send_form():
    return """
    <html>
    <head><title>Hi there</title></head>
    <body>
    <h1>Hello Anonymous</h1>
    <form method='get'>
        <input type='text' id='username' name='username' />
        <button type='submit'>Submit</button>
    </form>
    </body>
    </html>
    """