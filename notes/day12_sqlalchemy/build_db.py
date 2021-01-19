"""Building the DB"""

import csv
import os
from config import db
from models import Student


def build_db(filename):
    # Delete existing DB
    if os.path.exists(f"{filename}.sqlite3"):
        os.remove(f"{filename}.sqlite3")

    # Create DB structure
    db.create_all()

    # Add data to the DB
    with open(f"{filename}.csv") as f:
        content = csv.reader(f)
        next(content)
    
        for line in content:
            student = Student(
                name = line[0],
                major = line[1],
                gpa = line[2],
                gradyear = line[3]
            )
            db.session.add(student)
        db.session.commit()


def main():
    build_db("roster")

if __name__ == "__main__":
    main()
