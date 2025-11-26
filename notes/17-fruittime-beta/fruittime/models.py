#!/usr/bin/env python3

"""
Fruittime models

@author: CS330
@version: 2025.11
"""

import datetime

from flask_login import UserMixin
from marshmallow import fields
from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from fruittime import db, mm


class Base(DeclarativeBase): ...


class Fruit(db.Model):
    __tablename__ = "fruit"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False, unique=True)
    family: Mapped[str] = mapped_column()
    order: Mapped[str] = mapped_column()
    genus: Mapped[str] = mapped_column()
    calories: Mapped[float] = mapped_column()
    fat: Mapped[float] = mapped_column()
    sugar: Mapped[float] = mapped_column()
    carbohydrates: Mapped[float] = mapped_column()
    protein: Mapped[float] = mapped_column()

    reviews: Mapped[list["Review"]] = relationship(back_populates="fruit")

    def __repr__(self):
        return f"Fruit({self.name})"


class User(UserMixin, db.Model):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[str] = mapped_column(nullable=False)

    reviews: Mapped[list["Review"]] = relationship(back_populates="author")
    votes: Mapped[list["Vote"]] = relationship(back_populates="user")

    def __repr__(self):
        return f"User({self.name})"


class Review(db.Model):
    __tablename__ = "review"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    fruit_id: Mapped[int] = mapped_column(ForeignKey("fruit.id"))
    opinion: Mapped[str] = mapped_column(nullable=False)
    rating: Mapped[int] = mapped_column(nullable=False)
    date: Mapped[datetime.datetime] = mapped_column(nullable=False)

    fruit: Mapped["Fruit"] = relationship(back_populates="reviews")
    author: Mapped["User"] = relationship(back_populates="reviews")
    votes: Mapped[list["Vote"]] = relationship(back_populates="review")

    def __repr__(self):
        return f"Review(fruit={self.fruit}), author={self.author})"


class Vote(db.Model):
    __tablename__ = "vote"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    review_id: Mapped[int] = mapped_column(ForeignKey("review.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))

    user: Mapped["User"] = relationship(back_populates="votes")
    review: Mapped["Review"] = relationship(back_populates="votes")


class FruitSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Fruit
        include_relationships = True
        load_instance = True


class UserSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True


class ReviewSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        load_instance = True
        include_fk = True

    fruit = fields.Nested("FruitSchema")
    author = fields.Nested("UserSchema")


class VoteSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Vote
        include_fk = True
        load_instance = True

    review = fields.Nested("ReviewSchema")
    user = fields.Nested("UserSchema")
