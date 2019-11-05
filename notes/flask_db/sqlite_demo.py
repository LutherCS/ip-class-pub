#!/usr/bin/env python3
"""Working with SQLite3"""

import sqlite3
import sys


def read_txt(filename):
    """File format: ID Name Age Species Location"""
    zoo = []
    with open(filename, "r") as data:
        for line in data:
            zoo.append(tuple(line.strip().split(", ")))
    return zoo


def main(args):
    """Main function"""
    operation = args[1]
    conn = sqlite3.connect("zoo.sqlite3")
    cur = conn.cursor()
    if operation == "create":
        cur.execute("DROP TABLE IF EXISTS animal;")
        cur.execute("CREATE TABLE animal (id, name, age, species, location);")
        animals = read_txt("zoo.txt")
        cur.executemany("INSERT INTO animal VALUES(?, ?, ?, ?, ?);", animals)
        conn.commit()
    elif operation == "read":
        if len(args) > 2:
            species = (args[2], )
            cur.execute("SELECT * FROM animal WHERE species=?;", species)
        else:
            cur.execute("SELECT * FROM animal;")
        print("RESULTS")
        for animal in cur:
            print(animal)
    elif operation == "update":
        cur.execute("UPDATE animal SET age = age + 1;")
        conn.commit()
    elif operation == "delete":
        if len(args) > 2:
            species = (args[2], )
            cur.execute("DELETE FROM animal WHERE species=?;", species)
        else:
            cur.execute("DELETE FROM animal;")
        conn.commit()
    conn.close()


if __name__ == "__main__":
    main(sys.argv)
