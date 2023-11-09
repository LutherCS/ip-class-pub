#!/usr/bin/env python3
"""Working with SQLite3"""
import sqlite3
import csv

import click


@click.command()
@click.argument("db_name")
def create(db_name: str, datafile: str = "animal.csv") -> None:
    """Create database"""
    with open(datafile, "r", encoding="utf8") as f:
        data = csv.reader(f)
        headers = next(data)
        with sqlite3.connect(f"{db_name}.sqlite3") as conn:
            cur = conn.cursor()
            cur.execute("DROP TABLE IF EXISTS animal;")
            cur.execute(
                "CREATE TABLE animal ("
                + "id integer primary key,"
                + "name,"
                + "age integer,"
                + "species,"
                + "location);"
            )
            cur.executemany("INSERT INTO animal VALUES(?, ?, ?, ?, ?)", data)


@click.command()
@click.argument("db_name")
@click.option("--table", "-t", default="animal")
def read(db_name: str, table: str) -> None:
    """Read database"""
    with sqlite3.connect(f"{db_name}.sqlite3") as connection:
        cur = connection.cursor()
        cur.execute(f"SELECT * FROM {table};")
        print("RESULT")
        for record in cur:
            print(record)


@click.command(help="Querying the database by location and species")
@click.argument("db_name")
@click.option("--table", "-t", default="animal")
@click.option("--location", "-l")
@click.option("--species", "-s")
def query(db_name: str, table: str, location: str = "", species: str = "") -> None:
    """Query database"""
    with sqlite3.connect(f"{db_name}.sqlite3") as connection:
        cur = connection.cursor()
        if location and species:
            cur.execute(
                f"SELECT * FROM {table} WHERE location=? AND species=?;",
                (location, species),
            )
        elif location:
            cur.execute(f"SELECT * FROM {table} WHERE location=?;", (location,))
        elif species:
            cur.execute(
                f"SELECT * FROM {table} WHERE species LIKE ?;", (f"%{species}",)
            )
        else:
            cur.execute(f"SELECT * FROM {table};")
        print("RESULT")
        for record in cur:
            print(record)


@click.command()
@click.argument("db_name")
@click.option("--animal", "-a", type=int, default=0)
def update(db_name: str, animal: int) -> None:
    """Update database"""
    with sqlite3.connect(f"{db_name}.sqlite3") as connection:
        cur = connection.cursor()
        if animal > 0:
            cur.execute("UPDATE animal SET age = age + 1 WHERE id=?", (animal,))
        else:
            cur.execute("UPDATE animal SET age = age + 1")


@click.command()
@click.argument("db_name")
@click.option("--animal", "-a", type=int, default=0)
def delete(db_name: str, animal: int) -> None:
    """Delete records"""
    with sqlite3.connect(f"{db_name}.sqlite3") as connection:
        cur = connection.cursor()
        if animal > 0:
            cur.execute("DELETE FROM animal WHERE id=?", (animal,))
        else:
            cur.execute("DELETE FROM animal")


@click.group()
def cli():
    """Shell"""
    ...


def main():
    """Main function"""
    cli.add_command(create)
    cli.add_command(read)
    cli.add_command(update)
    cli.add_command(delete)
    cli.add_command(query)
    cli()


if __name__ == "__main__":
    main()
