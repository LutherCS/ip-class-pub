"""Flask basics"""

from flask import Flask, redirect, render_template, request, send_from_directory, url_for

app = Flask(__name__)

# library: list[dict[str, str | int]] = [
#     {"title": "Risk", "designer": "Albert Lamorisse", "year": 1957},
#     {"title": "Landlord", "designer": "Elizabeth Magie", "year": 1904},
#     {"title": "Landlord", "designer": "Theo", "year": 2026},
#     {"title": "Ticket to Ride", "designer": "Alan R. Moon", "year": 2004},
# ]
library: list[str] = []


@app.get("/")
def index():
    return render_template("index.jinja", all_games=library)


@app.get("/game/<int:idx>")
def game_by_id(idx: int):
    game = library[idx]
    return f"<strong>{game['title']}</strong> was designed by {game['designer']} in {game['year']}"


@app.get("/game/<string:title>")
def game_by_title(title: str):
    return "<br>".join(
        [str(game["title"]) for game in library if game["title"].lower() == title.lower()]
    )


@app.post("/addReview")
def add_game_review():
    library.append(request.form.get("title"))
    return render_template("reviews.jinja", all_games=library)
