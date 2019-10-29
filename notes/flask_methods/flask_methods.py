from flask import (
    Flask,
    render_template,
    request,
    make_response,
    redirect,
    url_for,
    send_from_directory,
)

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_user():
    pass
