#!/usr/bin/env python3
"""
PandAuth models

@author:
@version: 2025.12
"""

import datetime

from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column

from . import db, mm


# SQLAlchemy model
class User(UserMixin, db.Model):
    __tablename__ = "user"


# Marshmallow schema
class UserSchema(mm.SQLAlchemyAutoSchema):
    """User schema"""

    class Meta:
        """Metadata"""

        model = User
        include_relationships = True
