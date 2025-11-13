# Using Databases

Python comes with SQLite built-in but can work with many other Database Management Systems via connectors and adapters.

- SQLite3
- PostgreSQL (via `psycopg`)
- MongoDB (via `pymongo`)

## SQLite3

Built into Python3.
Simple yet powerful file-based database.

```python
import sqlite3

with sqlite3.connect("orchard.db") as conn:
    cur = conn.cursor()
    cur.execute("select * from fruit limit 10")
    rows = cur.fetchall()
    print(rows)
```

## `click`

We are going to interact with the database using `click` and turn `create`, `read`, `update`, and `delete` into commands that would work as follows:

```bash
$ python crud_sqlite.py
Options:
  --help  Show this message and exit.

Commands:
  create  Create a database from the data file
  delete  Delete records
  read    Read one or all records from the table fruit
  update  Update records
```

### Create

Create a database (*orchard.db*) using either *orchard.csv* or *orchard.json*.

```bash
$ python crud_sqlite.py create orchard.db --datafile orchard.csv
$ python crud_sqlite.py create orchard.db -d orchard.json
Done
```

### Read

Query the table *fruit* using an optional fruit id.

```bash
$ python crud_sqlite.py read orchard.db --fruit 35
(35, 'Apricot', 'Rosaceae', 'Rosales', 'Prunus', 15.0, 0.1, 3.2, 3.9, 0.5)
$ python crud_sqlite.py read orchard.db -f 35
(35, 'Apricot', 'Rosaceae', 'Rosales', 'Prunus', 15.0, 0.1, 3.2, 3.9, 0.5)
$ python crud_sqlite.py read orchard.db
```

### Update

Update the records in the table *fruit* using an optional fruit id.

```bash
$ python crud_sqlite.py update orchard.db --fruit 35
$ python crud_sqlite.py update orchard.db -f 35
$ python crud_sqlite.py update orchard.db
Done
```

### Delete

Delete the records from the table *fruit* using an optional fruit id.

```bash
$ python crud_sqlite.py delete orchard.db --fruit 35
$ python crud_sqlite.py delete orchard.db -f 35
$ python crud_sqlite.py delete orchard.db
Done
```

## Flask

We can use `click` commands using `callback` method in order to interact with the database from within the Flask application.

```python
import pathlib
from crud_sqlite import create
from flask import Flask

def create_app():
    app = Flask(__name__)
    if not pathlib.Path("orchard.db").exists():
        create.callback("orchard.db", "orchard.csv")

    return app
```

## References

- [sqlite3 — DB-API 2.0 interface for SQLite databases — Python 3.14.0 documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQLite Sample Database And Its Diagram (in PDF format)](http://www.sqlitetutorial.net/sqlite-sample-database/)
