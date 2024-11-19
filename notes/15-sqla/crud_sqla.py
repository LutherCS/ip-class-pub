#!/usr/bin/env python3
"""Building the DB using SQLAlchemy"""

import csv
import logging
import pathlib

import click
import sqlalchemy as sqla
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.orm import (
    DeclarativeBase,
    backref,
    relationship,
    scoped_session,
    sessionmaker,
)


class Base(DeclarativeBase): ...


class Animal(Base):
    __tablename__ = "animal"
    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String, nullable=False)
    age = sqla.Column(sqla.Integer)
    species = sqla.Column(sqla.String)
    location_id = sqla.Column(sqla.Integer, sqla.ForeignKey("location.id"))
    location = relationship("Location", backref=backref("location"))

    def __repr__(self):
        return f"<Animal(name={self.name!r}), location={self.location!r}>"


class Location(Base):
    __tablename__ = "location"
    id = sqla.Column(sqla.Integer, primary_key=True)
    name = sqla.Column(sqla.String, nullable=False, unique=True)

    def __repr__(self):
        return f"<Location(name={self.name!r})>"


class AnimalSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Animal
        include_relationships = True
        load_instance = True

    location = fields.Nested("LocationSchema")


class LocationSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Location
        include_fk = True
        load_instance = True


@click.command(help="Create a database from the CSV file")
@click.pass_context
def create(ctx) -> None:
    """Create database"""
    engine = ctx.obj["engine"]
    session = ctx.obj["session"]
    filename = ctx.obj["filename"]
    # Delete existing DB
    if pathlib.Path(f"{filename}.sqlite3").exists():
        pathlib.Path(f"{filename}.sqlite3").unlink()
    # TODO: Build tables
    Base.metadata.create_all(engine)
    # Add data to the DB
    # TODO: Add data
    with open(f"{filename}.csv", "r", encoding="utf-8") as f:
        content = csv.DictReader(f, delimiter=",")
        for item in content:
            location = Location(name=item["location"])
            existing_location = (
                session.query(Location).filter_by(name=location.name).first()
            )
            if existing_location:
                location = existing_location
            else:
                session.add(location)
            animal = Animal(
                id=item["id"],
                name=item["name"],
                age=item["age"],
                species=item["species"],
                location=location,
            )
            session.add(animal)
        session.commit()
    print("Database created successfully.")


@click.command(help="Read all records from the database")
@click.pass_context
def read(ctx) -> None:
    """Read all records"""
    session = ctx.obj["session"]
    print(f"{'id':5s}{'name':20s}{'age':5s}{'species':25s}{'location':15s}")
    # TODO: Get data
    zoo = session.query(Animal).all()
    schema = AnimalSchema(many=True)
    for animal in schema.dump(zoo):
        print(
            f"{animal["id"]:<5d}"
            + f"{animal['name']:20s}"
            + f"{animal['age']:<5d}"
            + f"{animal['species']:25s}"
            + f"{animal['location']["name"]}"
        )


@click.group()
@click.option("--verbose", "-v", is_flag=True, default=False)
@click.argument("filename")
@click.pass_context
def cli(ctx, verbose: bool, filename: str) -> None:
    """Command-line interface"""
    ctx.ensure_object(dict)
    if verbose:
        logging.basicConfig(level=logging.INFO)
    this_dir = pathlib.Path(__file__).parent
    engine = sqla.create_engine(f"sqlite:////{this_dir}/{filename}.sqlite3")
    session = scoped_session(sessionmaker(bind=engine))
    ctx.obj["session"] = session
    ctx.obj["engine"] = engine
    ctx.obj["filename"] = filename


def main():
    """Main function"""
    cli.add_command(create)
    cli.add_command(read)
    cli()


if __name__ == "__main__":
    main()
