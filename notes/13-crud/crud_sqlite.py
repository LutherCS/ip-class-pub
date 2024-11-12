#!/usr/bin/env python3
"""Working with SQLite3"""

import csv
import logging
import sqlite3

import click


@click.command(help="Create a database from the CSV file")
@click.argument("db_name")
@click.option("--datafile", default="menagerie.csv")
@click.option("--verbose", "-v", is_flag=True, default=False)
def create(db_name: str, datafile: str, verbose: bool) -> None:
    """Create database"""
    print("Creating a database")
    with sqlite3.connect(db_name) as conn:
        with open(datafile, "r") as f:
            data = csv.reader(f)
            headers = next(data)
            cursor = conn.cursor()
            cursor.execute("DROP TABLE IF EXISTS animal;")
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS animal ("
                + "id integer primary key, "
                + "name TEXT, "
                + "age integer, "
                + "species TEXT, "
                + "location TEXT)"
            )
            cursor.executemany("INSERT INTO animal VALUES(?, ?, ?, ?, ?)", data)


@click.command(help="Read all records from the specified table")
@click.argument("db_name")
@click.option("--table", "-t", default="animal")
def read(db_name: str, table: str) -> None:
    """Read all records"""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        # for record in cursor.fetchall():
        for record in cursor:
            print(record)


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
@click.option("--animal", "-a", help="Animal to delete", type=int, default=0)
@click.option("--species", "-s", help="Species to delete")
def delete(db_name: str, animal: int, species: str = "") -> None:
    """Delete records"""
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        if animal > 0:
            cursor.execute("DELETE FROM animal WHERE id=?;", (animal,))
        elif species:
            cursor.execute("DELETE FROM animal WHERE species=?;", (species,))
        else:
            cursor.execute("DELETE FROM animal;")


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
