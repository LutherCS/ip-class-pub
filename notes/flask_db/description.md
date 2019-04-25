# Using Flask and Databases

Python comes with SQLite built-in but can work with many other Database Management Systems via connectors and adapters.

* SQLite3
* MySQL
* PostgreSQL
* MongoDB

## SQLite3

Built into Python3. Simple yet powerful file-based database.

```python
import sqlite3

conn = sqlite3.connect("chinook.db")
cur = conn.cursor()
cur.execute("select * from artists limit 10")
rows = cur.fetchall()
print(rows)
```

## PostgreSQL

Use psycopg2

```bash
pip install psycopg2
```

Default post is 5432. This is one way to establish a connection.

```python
conn = psycopg2.connect(user="yasiro01", host="knuth.luther.edu", port=5432, dbname="world")
```

Another way to connect to a database is to specify its URL.

```python
import psycopg2

conn = psycopg2.connect("postgresql://yasiro01:@knuth.luther.edu/world")
cur = conn.cursor()
cur.execute("select * from country limit 10")
rows = cur.fetchall()
print(rows)
```

## Using records to work with PostgreSQL

Records is a wrapper around `psycopg2` from the author of `requests`.

```bash
pip install records
```

Connect to the database and execute a query.

```python
import records

db = records.Database("postgresql://yasiro01:@knuth.luther.edu/world")
rows = db.query("select * from country limit 10")
print(rows.all())
```

## Possible problems and solutions

You program may raise the following error: **ConnectionError("Could not connect to the database")**. The reason is usually security and there is nothing much you can do about it. The solution is to establish a tunnel

* LCWireless not allowed
* Connection from certain locations is not allowed

### Tunnel solution

Create an *ssh-tunnel*.

```bash
ssh -f yasiro01@knuth.luther.edu -L 2345:localhost:5432 -N
```

Change the connection parameters in your code.

```python
conn = psycopg2.connect(user="yasiro01", host="localhost", port=2345, dbname="world")
```

## References

* [sqlite3 — DB-API 2.0 interface for SQLite databases — Python 3.7.1 documentation](https://docs.python.org/3/library/sqlite3.html)
* [SQLite Sample Database And Its Diagram (in PDF format)](http://www.sqlitetutorial.net/sqlite-sample-database/)
* [Psycopg – PostgreSQL database adapter for Python — Psycopg 2.8.dev0 documentation](http://initd.org/psycopg/docs/)
* [Psycopg2 Tutorial - PostgreSQL wiki](https://wiki.postgresql.org/wiki/Psycopg2_Tutorial)
* [Introducing Records: SQL for Humans™ — Kenneth Reitz](https://www.kennethreitz.org/essays/introducing-records-just-write-sql)
* [Tutorial — PyMongo 3.7.2 documentation](http://api.mongodb.com/python/current/tutorial.html)
