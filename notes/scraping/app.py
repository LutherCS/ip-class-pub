from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

BASE_URL = "https://www.luther.edu/catalog/curriculum/"
all_programs = {}


def get_programs():
    """Get all programs of the college"""
    response = requests.get(BASE_URL)

    if (
        response.status_code == 200
        and response.headers["Content-Type"].find("html") > -1
    ):
        raw_html = response.text
    else:
        print("Bad stuff")

    html = BeautifulSoup(raw_html, "html.parser")

    for program in html.select("div#contentSections ul > li > h4 > a"):
        p_name = program.text
        p_url = program["href"]
        all_programs[p_url] = p_name


def get_courses(url):
    """Get courses of the program"""
    response = requests.get(f"{BASE_URL}{url}")

    if response.status_code == 200 and response.headers["Content-Type"].find("html") > -1:
        raw_html = response.text
    else:
        print("Bad stuff")

    html = BeautifulSoup(raw_html, "html.parser")

    all_courses = {}
    for course in html.select("div.courseContainer"):
        c_number = course.select("h4 span.courseNumber")[0].text
        c_title = course.select("h4 span.courseTitle")[0].text
        c_prereqs = None
        try:
            if course.select("ul li")[1].text[0] == "P":
                c_prereqs = course.select("ul li")[1].text[15:]
        except IndexError as ie:
            print(ie)
        all_courses[c_number] = [c_title, c_prereqs]
    return all_courses


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        get_programs()
        return render_template("base.html", programs=all_programs)
    else:
        program_url = request.form.get("program")
        program_courses = get_courses(program_url)
        return render_template(
            "result.html", programs=all_programs, courses=program_courses
        )
