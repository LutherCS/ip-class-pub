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
    pass


if __name__ == "__main__":
    main(sys.argv)
