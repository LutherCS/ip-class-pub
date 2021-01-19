"""Flask app"""

from flask import render_template
from config import app
from models import Student, StudentSchema


@app.route("/")
def show_roster():
    roster = Student.query.all()
    student_schema = StudentSchema(many=True)
    return render_template("index.html", roster=student_schema.dump(roster))
