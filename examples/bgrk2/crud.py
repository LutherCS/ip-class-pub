#!/usr/bin/env python3


import sqlite3


def read_csv(filename: str) -> list[tuple]:
    """
    title,designer,publisher,year
    """
    all_games = []
    with open(filename, "r", encoding="utf-8") as data_file:
        data_file.readline()
        for line in data_file:
            record = [field.strip('"') for field in line.strip().split(",")]
            record[-1] = int(record[-1])
            all_games.append(tuple(record))
    return all_games


def create_db(filename_src: str, filename_dst: str) -> None:
    all_games = read_csv(filename_src)
    conn = sqlite3.connect(filename_dst)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS game;")
    cursor.execute(
        "CREATE TABLE game (title, designer, publisher, year integer, rating integer);"
    )
    for record in all_games:
        cursor.execute("INSERT INTO game VALUES(?, ?, ?, ?, ?)", (*record, 0))
    # cursor.executemany("INSERT INTO game VALUES(?, ?, ?, ?);", all_games)
    conn.commit()
    conn.close()


def filter_by_year(db_file, year: str) -> None:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM game WHERE year=?;", (year,))
    for title, name, pub, year, rating in cursor:
        print(title, name, pub, year, rating)
    conn.close()


def filter_by_title(db_file, title: str) -> None:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM game WHERE title=?;", (title,))
    for title, name, pub, year, rating in cursor:
        print(title, name, pub, year, rating)
    conn.close()


def delete_by_year(db_file, year: str) -> None:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM game WHERE year=?;", (year,))
    conn.commit()
    conn.close()


def update_rating(db_file, title: str, new_rating: int) -> None:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("UPDATE game SET rating=? WHERE title=?;", (new_rating, title))
    conn.commit()
    for title, name, pub, year, rating in cursor:
        print(title, name, pub, year, rating)
    conn.close()


def main():
    create_db("examples/bgrk2/data/games.csv", "examples/bgrk2/data/games.sqlite3")
    filter_by_year("examples/bgrk2/data/games.sqlite3", 1995)
    filter_by_title("examples/bgrk2/data/games.sqlite3", "Pandemic")
    update_rating("examples/bgrk2/data/games.sqlite3", "Pandemic", 4)
    filter_by_title("examples/bgrk2/data/games.sqlite3", "Pandemic")


if __name__ == "__main__":
    main()
