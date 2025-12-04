#!/usr/bin/env python3
"""
Test the models

@authors: Roman Yasinovskyy
@version: 2025.12
"""

import datetime
import pathlib
import sys
from importlib import util

import pytest

try:
    util.find_spec("exercises." + pathlib.Path(__file__).parts[-2], "authorization")
except ModuleNotFoundError:
    sys.path.append(f"{pathlib.Path(__file__).parents[2]}/")
finally:
    from exercises.authorization.panda.models import User


@pytest.mark.parametrize(
    "google_id, email, name, picture",
    [
        ("330", "panda@example.com", "Norse Panda", "https://"),
        ("1", "alice@example.com", "Aardvark Alice", "https://"),
        ("2", "bob@example.com", "Beaver Bob", "https://"),
    ],
)
def test_create_user(freezer, google_id: str, email: str, name: str, picture: str) -> None:
    """Create a user"""
    freezer.move_to("2025-12-9")
    user = User()
    user.id = google_id
    user.email = email
    user.name = name
    user.picture = picture
    user.registered = datetime.datetime.now()
    assert isinstance(user, User)
    assert user.email == email
    assert user.name == name
    assert user.picture == picture
    assert user.registered == datetime.datetime(2025, 12, 9)


if __name__ == "__main__":
    pytest.main(["-v", __file__])
