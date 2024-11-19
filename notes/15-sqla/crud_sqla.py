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


class Animal(Base): ...


class Location(Base): ...


class AnimalSchema(SQLAlchemyAutoSchema): ...


class LocationSchema(SQLAlchemyAutoSchema): ...


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
    # Add data to the DB
    # TODO: Add data
    print("Database created successfully.")


@click.command(help="Read all records from the database")
@click.pass_context
def read(ctx) -> None:
    """Read all records"""
    session = ctx.obj["session"]
    print(f"{'id':5s}{'name':20s}{'age':5s}{'species':25s}{'location':15s}")
    # TODO: Get data


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
