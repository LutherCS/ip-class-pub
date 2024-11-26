#!/usr/bin/env python3
"""
Tech market navigator data models

@authors: Roman Yasinovskyy
@version: 2024.11
"""

from flask_login import UserMixin

from navigator import db, mm


class Company(db.Model):
    __tablename__ = "company"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    revenue = db.Column(db.Float)
    employees = db.Column(db.Integer)
    country = db.Column(db.String)
    headquarters = db.Column(db.String)

    def __repr__(self):
        return f"<Company(name={self.name!r})>"


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False, unique=True)
    name = db.Column(db.String)
    password = db.Column(db.String)


class Favorite(db.Model):
    __tablename__ = "favorite"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    company_id = db.Column(db.Integer, db.ForeignKey("company.id"))


class CompanySchema(mm.SQLAlchemyAutoSchema):
    """Company schema"""

    class Meta:
        """Metadata"""

        model = Company
        include_relationships = True


class UserSchema(mm.SQLAlchemyAutoSchema):
    """User schema"""

    class Meta:
        """Metadata"""

        model = User
        include_relationships = True


class FavoriteSchema(mm.SQLAlchemyAutoSchema):
    """Favorite schema"""

    class Meta:
        """Metadata"""

        model = Favorite
        include_fk = True
