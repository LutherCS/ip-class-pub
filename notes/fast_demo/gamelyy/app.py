"""
GamelYY with FastAPI
App factory

@author: Roman Yasinovskyy
@version: 2026.11
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routes import main


def create_app():
    app = FastAPI()
    app.include_router(main)
    app.mount("/static", StaticFiles(directory="gamelyy/static"), name="static")
    return app


app = create_app()
