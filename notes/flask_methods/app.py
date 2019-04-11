from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def hello_user():
    if request.method == "GET":
        user_name = request.cookies.get("username")
        if user_name:
            return render_template("index.html", coursename="CS330", username=user_name)
        else:
            return render_template("login.html", coursename="CS330")
    else:
        response = make_response(redirect(url_for("hello_user"), code=303))
        if request.form.get("logout"):
            response.set_cookie("username", "", expires=0)
        else:
            response.set_cookie("username", request.form.get("username"))
        return response
