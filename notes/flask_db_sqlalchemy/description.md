# Using SQLAlchemy

Use ORM to interact with the database.

## Install necessary packages

```bash
pip install flask flask-sqlalchemy flask-marshmallow marshmallow-sqlalchemy
```

## Model the database schema

```python
class Animal(db.Model):
    __tablename__ = "ANIMAL"
    aid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer, default=0)
    species = db.Column(db.String)
    location = db.Column(db.Integer)
```

## Build the database

```python
db.create_all()
```

## Read the database

```python
zoo = Animal.query.all()
```

## References

* [Python REST APIs With Flask, Connexion, and SQLAlchemy – Part 2 – Real Python](https://realpython.com/flask-connexion-rest-api-part-2/)
