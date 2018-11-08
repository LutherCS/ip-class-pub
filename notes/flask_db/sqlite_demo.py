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
    operation = args[1]
    conn = sqlite3.connect("zoo.sqlite3")
    if operation == "create":
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS animal")
        cur.execute(
            """CREATE TABLE animal
                (id, name, age, species, location)"""
        )
        animals = read_txt("zoo.txt")
        cur.executemany("INSERT INTO animal VALUES (?,?,?,?,?)", animals)
        conn.commit()
    elif operation == "read":
        cur = conn.cursor()
        spec = (args[2],)
        cur.execute("SELECT * FROM animal WHERE species=?", spec)
        for row in cur:
            print(f"{row[3]} {row[1]} is {row[2]} y.o.")
    elif operation == "update":
        cur = conn.cursor()
        age_diff = (args[2], )
        cur.execute("UPDATE animal SET age = age + ?", age_diff)
        conn.commit()
    elif operation == "delete":
        cur = conn.cursor()
        spec = (args[2],)
        cur.execute("DELETE FROM animal WHERE species=?", spec)
        conn.commit()

    conn.close()


if __name__ == "__main__":
    main(sys.argv)
