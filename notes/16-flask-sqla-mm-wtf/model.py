#!/usr/bin/env python3
"""Data model"""

from config import db, mm
from flask_wtf import FlaskForm
from marshmallow import fields
from sqlalchemy.orm import backref, relationship
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired


class Animal(db.Model):
    """Animal model"""

    __tablename__ = "animal"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer)
    species = db.Column(db.String)
    location_id = db.Column(db.Integer, db.ForeignKey("location.id"))
    location = relationship("Location", backref=backref("location"))

    def __repr__(self):
        return f"<Animal(name={self.name!r}), location={self.location!r}>"


class Location(db.Model):
    """Location model"""

    __tablename__ = "location"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False, unique=True)

    def __repr__(self):
        return f"<Location(name={self.name!r})>"


class AnimalSchema(mm.SQLAlchemyAutoSchema):
    """Animal schema"""

    class Meta:
        model = Animal
        include_relationships = True
        load_instance = True

    location = fields.Nested("LocationSchema")


class LocationSchema(mm.SQLAlchemyAutoSchema):
    """Location schema"""

    class Meta:
        model = Location
        include_fk = True
        load_instance = True


class AnimalAddForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    age = IntegerField("Age", validators=[DataRequired()])
    species = StringField("Species", validators=[DataRequired()])
    location = StringField("Location", validators=[DataRequired()])
