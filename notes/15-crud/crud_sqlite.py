#!/usr/bin/env python3
"""Working with SQLite3"""

import csv
import json
import logging
import pathlib
import sqlite3

import click


@click.command(help="Create a database from the data file")
@click.argument("db_name")
@click.option("--datafile", "-d", default="orchard.csv")
@click.option("--verbose", "-v", is_flag=True, default=False)
def create(db_name: str, datafile: str, verbose: bool = False) -> None:
    """Create a database

    :param db_name: database name
    :param datafile: source datafile
    :param verbose: set verbosity to DEBUG level
    """


def create_from_csv(db_name: str, datafile: str) -> None:
    """Create a database from csv

    :param db_name: database name
    :param datafile: source datafile
    """


def create_from_json(db_name: str, datafile: str) -> None:
    """Create a database from csv

    :param db_name: database name
    :param datafile: source datafile
    """


@click.command(help="Read all records from the specified table")
@click.argument("db_name")
@click.option("--table", "-t", default="fruit")
def read(db_name: str, table: str) -> None:
    """Read all records from some table

    :param db_name: database name
    :param table: target table
    """


@click.command()
@click.argument("db_name")
@click.option("--fruit", "-f", help="fruit to update", type=int, default=0)
def update(db_name: str, fruit: int) -> None:
    """Update records

    :param db_name: database name
    :param fruit: target item
    """


@click.command()
@click.argument("db_name")
@click.option("--fruit", "-f", help="fruit to delete", type=int, default=0)
@click.option("--family", help="Family of fruits to delete")
def delete(db_name: str, fruit: int, family: str = "") -> None:
    """Delete records

    :param db_name: database name
    :param fruit: target item
    :param family: target fruit family
    """


@click.group()
def cli():
    """Command-line interface"""
    ...


def main():
    """Main function"""
    cli.add_command(create)
    cli.add_command(read)
    cli.add_command(update)
    cli.add_command(delete)
    cli()


if __name__ == "__main__":
    main()
