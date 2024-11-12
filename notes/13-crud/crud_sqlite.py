#!/usr/bin/env python3
"""Working with SQLite3"""

import csv
import logging
import sqlite3

import click


@click.command(help="Create a database from the CSV file")
@click.argument("db_name")
@click.option("--datafile", default="animal.csv")
@click.option("--verbose", "-v", is_flag=True, default=False)
def create(db_name: str, datafile: str, verbose: bool) -> None:
    """Create database"""


@click.command(help="Read all records from the specified table")
@click.argument("db_name")
@click.option("--table", "-t", default="animal")
def read(db_name: str, table: str) -> None:
    """Read all records"""


@click.command()
@click.argument("db_name")
@click.option("--table", "-t", default="animal")
@click.option("--location", "-l", help="Location to read")
@click.option("--species", "-s", help="Species to read")
def query(db_name: str, table: str, species: str = "", location: str = "") -> None:
    """Query records"""


@click.command()
@click.argument("db_name")
@click.option("--animal", "-a", help="Animal to update", type=int, default=0)
def update(db_name: str, animal: int) -> None:
    """Update records"""


@click.command()
@click.argument("db_name")
@click.option("--animal", "-a", help="Animal to update", type=int, default=0)
@click.option("--species", "-s", help="Species to delete")
def delete(db_name: str, animal: int, species: str = "") -> None:
    """Delete records"""


@click.group()
def cli():
    """Command-line interface"""
    ...


def main():
    """Main function"""
    cli.add_command(create)
    cli.add_command(read)
    cli.add_command(query)
    cli.add_command(update)
    cli.add_command(delete)
    cli()


if __name__ == "__main__":
    main()
