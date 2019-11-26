#!/usr/bin/env python
"""Data models"""

from config import db, ma


class Animal(db.Model):
    __tablename__ = "ANIMAL"
    aid = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    age = db.Column(db.Integer, default=0)
    species = db.Column(db.String)
    location = db.Column(db.Integer)


class AnimalSchema(ma.ModelSchema):
    class Meta:
        model = Animal
        sqla_session = db.session
