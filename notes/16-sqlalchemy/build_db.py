#!/usr/bin/env python3
"""Build the database"""

import csv
import pathlib

import sqlalchemy as sa
from sqlalchemy.orm import scoped_session, sessionmaker

from models import Animal

def init_db(filename: str):
    """Initialize the database"""
    this_dir = pathlib.Path(__file__).parent
    if pathlib.Path(f"{this_dir}/{filename}.sqlite3").exists():
        pathlib.Path(f"{this_dir}/{filename}.sqlite3").unlink()
    engine = sa.create_engine(f"sqlite:////{this_dir}/{filename}.sqlite3")
    session = scoped_session(sessionmaker(bind=engine))

    Animal.metadata.create_all(engine)

    with open(f"{filename}.csv", "r", encoding="utf8") as f:
        content = csv.DictReader(f)
        for item in content:
            an_animal = Animal(
                an_id=item["id"],
                name=item["name"],
                age=item["age"],
                species=item["species"],
                location=item["location"],
            )
            session.add(an_animal)
        session.commit()


def main():
    """This is the main function"""
    init_db("zoo")


if __name__ == "__main__":
    main()
