from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, CS3330!"


@app.route("/bye/<string:name>")
def bye(name):
    return f"Bye, {name}"


if __name__ == "__main__":
    app.run()
