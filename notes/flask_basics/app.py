from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello_world():
    audience = "CS330"
    return f"Hello, <strong>{audience}</strong>!"


@app.route("/number/<int:n>")
def add_1(n: int):
    return f"{n} + 1 = {n + 1}"


@app.route("/user/<string:name>")
def greet_by_name(name):
    return f"Hello, {name}"


@app.route("/hello")
def hello_form():
    if "firstname" in request.args:
        return greet_by_name(request.args["firstname"])
    else:
        return send_form()


def send_form():
    return """
            <form method='get'>
                <label for='firstname'>Enter yo0ur name</label>
                <input id='firstname' type='text' name='firstname' />
                <input type='submit' />
            </form>
    """

