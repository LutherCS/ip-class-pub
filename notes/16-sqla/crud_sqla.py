#!/usr/bin/env python3
"""Building the DB using SQLAlchemy"""

import csv
import datetime
import logging
import pathlib

import click
import sqlalchemy as sqla
from sqlalchemy import Column, Float, ForeignKey, Integer, String, DateTime
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.orm import (
    DeclarativeBase,
    backref,
    relationship,
    scoped_session,
    sessionmaker,
)


class Base(DeclarativeBase): ...


class Fruit(Base):
    __tablename__ = "fruit"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    family = Column(String(50))
    order = Column(String(50))
    genus = Column(String(50))
    calories = Column(Float)
    fat = Column(Float)
    sugar = Column(Float)
    carbohydrates = Column(Float)
    protein = Column(Float)

    def __repr__(self):
        return f"Fruit({self.name})"


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)

    def __repr__(self):
        return f"Author({self.name})"


class Review(Base):
    __tablename__ = "review"

    id = Column(Integer, primary_key=True, nullable=False)
    author_id = Column(Integer, ForeignKey("author.id"))
    fruit_id = Column(Integer, ForeignKey("fruit.id"))
    opinion = Column(String)
    rating = Column(Integer)
    date = Column(DateTime)

    fruit = relationship("Fruit")
    author = relationship("Author")

    def __repr__(self):
        return f"Review(fruit={self.fruit}), author={self.author}"


class FruitSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Fruit
        include_relationships = True


class AuthorSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Author
        include_relationships = True


class ReviewSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Review
        include_relationships = True
        include_fk = True

    fruit = fields.Nested("FruitSchema")
    author = fields.Nested("AuthorSchema")


@click.command(help="Create a database from the CSV file")
@click.pass_context
def create(ctx) -> None:
    """Create database"""
    engine = ctx.obj["engine"]
    session = ctx.obj["session"]
    filename = ctx.obj["filename"]
    # Delete existing DB
    if pathlib.Path(f"{filename}.sqlite3").exists():
        pathlib.Path(f"{filename}.sqlite3").unlink()
    # Build tables
    Base.metadata.create_all(engine)
    # TODO: Add data
    with open(f"{filename}.csv", "r", encoding="utf8") as f:
        content = csv.DictReader(f, delimiter=",")
        for item in content:
            fruit = Fruit(
                id=item["id"],
                name=item["name"],
                family=item["family"],
                order=item["order"],
                genus=item["genus"],
                calories=item["calories"],
                fat=item["fat"],
                sugar=item["sugar"],
                carbohydrates=item["carbohydrates"],
                protein=item["protein"],
            )
            session.add(fruit)
        session.commit()
    for raw_review in [
        ("Susan", "Mango", "Sweet", 4),
        ("Bob", "Durian", "Stinky", 2),
        ("Susan", "Durian", "AWESOME", 4),
    ]:
        author = Author(name=raw_review[0])
        existing_author = session.query(Author).filter_by(name=author.name).first()
        if existing_author:
            author = existing_author
        else:
            session.add(author)
        fruit_name = raw_review[1]
        existing_fruit = session.query(Fruit).filter_by(name=fruit_name).first()
        if existing_fruit:
            fruit = existing_fruit
        else:
            raise ValueError("Unknown Fruit")
        review = Review(
            author=author,
            fruit=fruit,
            opinion=raw_review[2],
            rating=raw_review[3],
        )
        session.add(review)
    session.commit()

    print("Database created successfully.")


@click.command(help="Read all records from the database")
@click.pass_context
def read(ctx) -> None:
    """Read all records"""
    session = ctx.obj["session"]
    print(f"{'review':10s}{'author':10s}{'fruit':10s}")
    # TODO: Get data


@click.group()
@click.option("--verbose", "-v", is_flag=True, default=False)
@click.argument("filename")
@click.pass_context
def cli(ctx, verbose: bool, filename: str) -> None:
    """Command-line interface"""
    ctx.ensure_object(dict)
    if verbose:
        logging.basicConfig(level=logging.INFO)
    this_dir = pathlib.Path(__file__).parent
    engine = sqla.create_engine(f"sqlite:////{this_dir}/{filename}.sqlite3")
    session = scoped_session(sessionmaker(bind=engine))
    ctx.obj["session"] = session
    ctx.obj["engine"] = engine
    ctx.obj["filename"] = filename


def main():
    """Main function"""
    cli.add_command(create)
    cli.add_command(read)
    cli()


if __name__ == "__main__":
    main()
