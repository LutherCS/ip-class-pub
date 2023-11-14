#!/usr/bin/env python3
"""Models"""

import sqlalchemy as sa
from sqlalchemy.orm import declarative_base
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field

Base = declarative_base()


class Animal(Base):
    """Animal class"""

    __tablename__ = "animal"
    an_id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    age = sa.Column(sa.Integer)
    species = sa.Column(sa.String)
    location = sa.Column(sa.String)

    def __repr__(self):
        return f"<Animal(name={self.name!r})>"


class AnimalSchema(SQLAlchemySchema):
    """Animal schema"""

    class Meta:
        """Animal metadata"""

        model = Animal
        load_instance = True

    an_id = auto_field()
    name = auto_field
    age = auto_field
    species = auto_field
    location = auto_field
