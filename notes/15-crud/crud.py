#!/usr/bin/env python3
"""Working with SQLite3"""
import sqlite3
import csv


def main():
    with open("animal.csv", "r", encoding="utf8") as f:
        data = csv.DictReader(f.readlines())
        with sqlite3.connect("zoo.sqlite3") as conn:
            cur = conn.cursor()
            cur.execute("DROP TABLE IF EXISTS animal;")
            cur.execute("CREATE TABLE animal (id, name, age, species, location);")
            for animal in data:
                cur.execute(
                    "INSERT INTO animal VALUES(?, ?, ?, ?, ?)",
                    (
                        animal["id"],
                        animal["name"],
                        animal["age"],
                        animal["species"],
                        animal["location"],
                    ),
                )


if __name__ == "__main__":
    main()
