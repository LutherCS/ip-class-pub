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
    if request.method == "GET":
        user_name = request.cookies.get("username")
        if user_name:
            return render_template("index.html", username=user_name)
        else:
            return render_template("login.html")
    else:  # POST
        response = make_response(redirect(url_for("hello_user"), code=303))

        if request.form.get("logout"):
            response.set_cookie("username", "", expires=0)
        else:
            response.set_cookie("username", request.form.get("username"))

        return response


@app.route("/css/<path:some_path>")
def serve_css(some_path):
    return send_from_directory("static/css", some_path)


@app.route("/js/<path:some_path>")
def serve_js(some_path):
    return send_from_directory("static/js", some_path)
