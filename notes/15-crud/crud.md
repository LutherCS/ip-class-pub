# Using Databases

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

Use psycopg

```bash
pip install psycopg
```

Default post is 5432. This is one way to establish a connection.

```python
conn = psycopg.connect(user="username", host="knuth.luther.edu", port=5432, dbname="world")
```

Another way to connect to a database is to specify its URL.

```python
import psycopg

conn = psycopg.connect("postgresql://username:@knuth.luther.edu/world")
cur = conn.cursor()
cur.execute("select * from country limit 10")
rows = cur.fetchall()
print(rows)
```

## Possible problems and solutions

You program may raise the following errors:

```bash
ConnectionError("Could not connect to the database")
```

or

```bash
psycopg.OperationalError: connection failed: server closed the connection unexpectedly
```

The reason is usually security and there is nothing much you can do about it.
The solution is to establish a tunnel.

* LCWireless not allowed
* Connection from certain locations is not allowed

### Tunnel solution

Create an *ssh-tunnel*.

```bash
ssh -f username@knuth.luther.edu -L 2345:localhost:5432 -N
```

Change the connection parameters in your code.

```python
conn = psycopg.connect(user="username", host="localhost", port=2345, dbname="world")
```

Once done, check the id of the process responsible for the tunnel and kill it.
Use `ps` to find the process or `ss` to see open ssh session(s).

```bash
ps -C ssh
kill
```

## References

* [sqlite3 — DB-API 2.0 interface for SQLite databases — Python 3.7.1 documentation](https://docs.python.org/3/library/sqlite3.html)
* [SQLite Sample Database And Its Diagram (in PDF format)](http://www.sqlitetutorial.net/sqlite-sample-database/)
* [psycopg 3.2.0.dev1 documentation](https://www.psycopg.org/psycopg3/docs/)
[Basic module usage - psycopg 3.2.0.dev1 documentation](https://www.psycopg.org/psycopg3/docs/basic/usage.html)
* [Tutorial — PyMongo 3.7.2 documentation](http://api.mongodb.com/python/current/tutorial.html)
