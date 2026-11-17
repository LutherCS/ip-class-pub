"""
GamelYY model

@author: Roman Yasinovskyy
@version: 2026.11
"""

from flask_marshmallow.sqla import SQLAlchemyAutoSchema
from marshmallow import fields
from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, relationship


class Base(DeclarativeBase): ...


class Game(Base):
    __tablename__ = "game"

    rank = Column(Integer)
    bgg_url = Column(String)
    game_id = Column(Integer, primary_key=True)
    names = Column(String, nullable=False)
    min_players = Column(Integer)
    max_players = Column(Integer)
    avg_time = Column(Integer)
    min_time = Column(Integer)
    max_time = Column(Integer)
    year = Column(Integer)
    avg_rating = Column(Float)
    geek_rating = Column(Float)
    num_votes = Column(Integer)
    image_url = Column(String)
    age = Column(Integer)
    mechanic = Column(String)
    owned = Column(Integer)
    category = Column(String)
    designer = Column(String)
    weight = Column(Float)


class User(Base):
    __tablename__ = "user"

    username = Column(String(20), primary_key=True)
    password = Column(String)


class Ownership(Base):
    __tablename__ = "ownership"

    id = Column(Integer, primary_key=True)
    user_id = Column(String)
    game_id = Column(Integer)

    game = relationship("Game")
    user = relationship("User")


class GameSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Game
        include_relationships = True


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True


class OwnershipSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Ownership
        include_relationships = True
        include_fk = True

    game = fields.Nested("GameSchema")
    user = fields.Nested("UserSchema")


def create(): ...


def retrieve(): ...


def update(): ...


def delete(): ...


def main(): ...


if __name__ == "__main__":
    main()
