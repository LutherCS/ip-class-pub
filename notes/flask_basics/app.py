"""Flask basics"""

from flask import Flask, redirect, send_from_directory, url_for

app = Flask(__name__)

library: list[dict[str, str | int]] = [
    {"title": "Risk", "designer": "Albert Lamorisse", "year": 1957},
    {"title": "Landlord", "designer": "Elizabeth Magie", "year": 1904},
    {"title": "Landlord", "designer": "Theo", "year": 2026},
    {"title": "Ticket to Ride", "designer": "Alan R. Moon", "year": 2004},
]


@app.get("/")
def index():
    return "Hello, CS330"


@app.get("/hello/<string:name>")
def hello(name: str):
    return f"Hello, {name}"


@app.get("/hello/<int:number>")
def plus2(number: int):
    return f"{number} incremented by 2 is {number + 2}"


@app.get("/game/<int:idx>")
def game_by_id(idx: int):
    game = library[idx]
    return f"<strong>{game['title']}</strong> was designed by {game['designer']} in {game['year']}"


@app.get("/game/<string:title>")
def game_by_title(title: str):
    return "<br>".join(
        [str(game["title"]) for game in library if game["title"].lower() == title.lower()]
    )


@app.get("/api/game/<int:idx>")
def game_by_id_api(idx: int):
    return library[idx]


@app.get("/api/game/<string:title>")
def game_by_title_api(title: str):
    return [game for game in library if game["title"].lower() == title.lower()]


@app.get("/demo/<string:filename>")
def demo(filename: str):
    return send_from_directory("static", path=filename)


@app.get("/demo/")
def demo_index():
    return redirect(url_for("demo", filename="index.html"))
