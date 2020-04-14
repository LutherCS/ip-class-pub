#!/usr/bin/env python3
"""Working with SQLite3"""


import sqlite3
import sys
import pandas as pd


def create_db(*argv):
    conn, dbname, _ = argv
    print(f"Adding data to the database {dbname}")
    raise NotImplementedError


def read_db(*argv):
    conn, dbname, major = argv
    print(f"Reading data from the database {dbname}")
    raise NotImplementedError


def update_db(*argv):
    conn, dbname, _ = argv
    print(f"Updating data in the database {dbname}")
    raise NotImplementedError


def delete_db(*argv):
    conn, dbname, major = argv
    print(f"Deleting data from the database {dbname}")
    raise NotImplementedError


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
    else:
        raise NotImplementedError



if __name__ == "__main__":
    main(sys.argv)
