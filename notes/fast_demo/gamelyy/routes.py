"""
GamelYY with FastAPI
Routes

@author: Roman Yasinovskyy
@version: 2026.11
"""

from typing import Annotated

from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from .config import settings
from .logic import game_lookup

main = APIRouter()
templates = Jinja2Templates(directory="gamelyy/templates")


@main.get("/")
def index(request: Request):
    return templates.TemplateResponse(request, "reviews.jinja", {"all_games": settings.shelf})


@main.post("/addGame")
def add_game_review(title: Annotated[str, Form()]):
    new_game = game_lookup(title)
    settings.shelf.add(new_game)
    return RedirectResponse(main.url_path_for("index"), status_code=302)


@main.get("/game/{title}")
def game_details(title: str):
    new_game = game_lookup(title)
    return new_game
