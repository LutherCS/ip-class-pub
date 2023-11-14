#!/usr/bin/env python3
"""Build the database"""

import csv
import pathlib

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field


Base = declarative_base()


class Animal(Base):
    """Animal class"""

    __tablename__ = "animal"
    an_id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    age = sa.Column(sa.Integer)
    species = sa.Column(sa.String)
    location = sa.Column(sa.String)

    def __repr__(self):
        return f"<Animal(name={self.name!r})>"


class AnimalSchema(SQLAlchemySchema):
    """Animal schema"""

    class Meta:
        """Animal metadata"""

        model = Animal
        load_instance = True

    an_id = auto_field()
    name = auto_field
    age = auto_field
    species = auto_field
    location = auto_field


def init_db(filename: str):
    """Initialize the database"""
    this_dir = pathlib.Path(__file__).parent
    if pathlib.Path(f"{this_dir}/{filename}.sqlite3").exists():
        pathlib.Path(f"{this_dir}/{filename}.sqlite3").unlink()
    engine = sa.create_engine(f"sqlite:////{this_dir}/{filename}.sqlite3")
    session = scoped_session(sessionmaker(bind=engine))

    Base.metadata.create_all(engine)

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
