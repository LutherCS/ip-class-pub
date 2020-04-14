#!/usr/bin/env python3
"""Working with SQLite3"""


import sqlite3
import sys
import pandas as pd


def create_db(*argv):
    conn, dbname, _ = argv
    print(f"Adding data to the database {dbname}")
    conn.execute(f"drop table if exists {dbname}")
    data = pd.read_csv(f"{dbname}.csv")
    data.to_sql(f"{dbname}", conn)


def read_db(*argv):
    conn, dbname, major = argv
    print(f"Reading data from the database {dbname}")
    cur = conn.cursor()
    if major:
        cur.execute(f"select * from {dbname} where Major=?", (major,))
    else:
        cur.execute(f"select * from {dbname}")
    print(f"{'Name':20}{'Major':20}{'GPA':5}{'Class':5}")
    print("-" * 50)
    for idx, name, major, gpa, year in cur:
        print(f"{name:20}{major:<20}{gpa:3.2f}{year:>5}")


def update_db(*argv):
    conn, dbname, _ = argv
    print(f"Updating data in the database {dbname}")
    cur = conn.cursor()
    cur.execute(f"update {dbname} set GradYear = GradYear + 1 where GradYear=2020")


def delete_db(*argv):
    conn, dbname, major = argv
    print(f"Deleting data from the database {dbname}")
    cur = conn.cursor()
    if major:
        cur.execute(f"delete from {dbname} where Major=?", (major,))
    else:
        cur.execute(f"delete from {dbname}")


def main(args):
    """Main function"""
    operations = {
        "create": create_db,
        "read": read_db,
        "update": update_db,
        "delete": delete_db,
    }

    if len(args) < 2:
        print("Please provide a database name")
    elif len(args) < 3:
        print("Please tell what do you want to do with the db")
    else:
        dbname = args[1]
        op = args[2]
        param = None
        if len(args) > 3:
            param = args[3]
        with sqlite3.connect(f"{dbname}.db") as conn:
            operations[op](conn, dbname, param)


if __name__ == "__main__":
    main(sys.argv)
