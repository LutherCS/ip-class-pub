#!/usr/bin/env python

"""Using SQLAlchemy to access a database"""

import csv
import os
from config import db
from models import Animal


def read_csv(filename):
    """File format: ID Name Age Species Location"""
    pass


def build_db(filename):
    """
    Create a new database from CSV
    1. Delete the database file
    2. Create the database structure
    3. Populate the database
    """
    pass


def main():
    """Main function"""
    build_db("zoo")


if __name__ == "__main__":
    main()
