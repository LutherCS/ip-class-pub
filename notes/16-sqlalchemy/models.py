#!/usr/bin/env python3
"""Models"""

from config import db, ma


class Animal(db.Model):
    """Animal class"""

    __tablename__ = "animal"
    an_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    species = db.Column(db.String)
    location = db.Column(db.String)

    def __repr__(self):
        return f"<Animal(name={self.name!r})>"


class AnimalSchema(ma.SQLAlchemySchema):
    """Animal schema"""

    class Meta:
        """Animal metadata"""

        model = Animal
        load_instance = True

    an_id = ma.auto_field()
    name = ma.auto_field()
    age = ma.auto_field()
    species = ma.auto_field()
    location = ma.auto_field()
