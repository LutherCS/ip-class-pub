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


class Location(db.Model):
    """Location model"""


class AnimalSchema(mm.SQLAlchemyAutoSchema):
    """Animal schema"""


class LocationSchema(mm.SQLAlchemyAutoSchema):
    """Location schema"""
