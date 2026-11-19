"""
GamelYY model

@author: Roman Yasinovskyy
@version: 2026.11
"""

import csv

from marshmallow import fields
from sqlalchemy import ForeignKey
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from gamelyy import db, mm


class Base(DeclarativeBase): ...


class Game(db.Model):
    __tablename__ = "game"

    rank: Mapped[int] = mapped_column()
    bgg_url: Mapped[str] = mapped_column()
    game_id: Mapped[int] = mapped_column(primary_key=True)
    names: Mapped[str] = mapped_column(nullable=False)
    min_players: Mapped[int] = mapped_column()
    max_players: Mapped[int] = mapped_column()
    avg_time: Mapped[int] = mapped_column()
    min_time: Mapped[int] = mapped_column()
    max_time: Mapped[int] = mapped_column()
    year: Mapped[int] = mapped_column()
    avg_rating: Mapped[float] = mapped_column()
    geek_rating: Mapped[float] = mapped_column()
    num_votes: Mapped[int] = mapped_column()
    image_url: Mapped[str] = mapped_column()
    age: Mapped[int] = mapped_column()
    mechanic: Mapped[str] = mapped_column()
    owned: Mapped[int] = mapped_column()
    category: Mapped[str] = mapped_column()
    designer: Mapped[str] = mapped_column()
    weight: Mapped[float] = mapped_column()


class User(db.Model):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(primary_key=True)
    password: Mapped[str] = mapped_column()


class Ownership(db.Model):
    __tablename__ = "ownership"

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[str] = mapped_column(ForeignKey("user.username"))
    game_id: Mapped[int] = mapped_column(ForeignKey("game.game_id"))

    game: Mapped["Game"] = relationship("Game")
    user: Mapped["User"] = relationship("User")


class GameSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Game
        include_relationships = True


class UserSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True


class OwnershipSchema(mm.SQLAlchemyAutoSchema):
    class Meta:
        model = Ownership
        include_relationships = True
        include_fk = True

    game = fields.Nested("GameSchema")
    user = fields.Nested("UserSchema")


def load_data(filename: str):
    with open(filename) as f:
        content = csv.DictReader(f)
        try:
            for item in content:
                game = Game()
                game.rank = int(item["rank"])
                game.bgg_url = item["bgg_url"]
                game.game_id = int(item["game_id"])
                game.names = item["names"]
                game.min_players = int(item["min_players"])
                game.max_players = int(item["max_players"])
                game.avg_time = int(item["avg_time"])
                game.min_time = int(item["min_time"])
                game.max_time = int(item["max_time"])
                game.year = int(item["year"])
                game.avg_rating = float(item["avg_rating"])
                game.geek_rating = float(item["geek_rating"])
                game.num_votes = int(item["num_votes"])
                game.image_url = item["image_url"]
                game.age = int(item["age"])
                game.mechanic = item["mechanic"]
                game.owned = int(item["owned"])
                game.category = item["category"]
                game.designer = item["designer"]
                game.weight = float(item["weight"])
                db.session.add(game)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def add_anonymous_user():
    try:
        anonymous = User()
        anonymous.username = "anonymous"
        anonymous.password = ""
        db.session.add(anonymous)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
