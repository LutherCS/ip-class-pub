"""
fast jokes api routes

@author:
@version: 2026.11
"""

from fastapi import APIRouter, HTTPException

from .logic import Joker

router = APIRouter()


@router.get("/{language}/{category}/all")
def get_all_jokes_by_language_and_category(language: str, category: str):
    """Get all jokes in the specified language/category combination

    :param language: language of the joke
    :param category: category of the joke
    """
    # TODO: Implement this function


@router.get("/{language}/{category}/{number}")
def get_n_jokes_by_language_and_category(language: str, category: str, number: int):
    """Get multiple jokes

    :param language: language of the jokes
    :param category: category of the jokes
    :param number: number of the jokes to return
    """
    # TODO: Implement this function


@router.get("/{joke_id}")
def get_the_joke(joke_id: int):
    """Get a specific joke by id

    :param joke_id: joke id
    """
    # TODO: Implement this function
