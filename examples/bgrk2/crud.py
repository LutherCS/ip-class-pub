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
            all_games.append(tuple(record))
    return all_games


def create_db(filename_src: str, filename_dst: str) -> None:
    all_games = read_csv(filename_src)
    conn = sqlite3.connect(filename_dst)
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS game;")
    cursor.execute("CREATE TABLE game (title, designer, publisher, year)")
    # for record in all_games:
    #     cursor.execute("INSERT INTO game VALUES(?, ?, ?, ?)", record)
    cursor.executemany("INSERT INTO game VALUES(?, ?, ?, ?)", all_games)
    conn.commit()
    conn.close()


def filter_by_year(db_file, year: str) -> None:
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM game WHERE year='{year}'")
    for title, name, pub, year in cursor:
        print(title, name, pub, year)
    conn.close()


def main():
    create_db("data/games.csv", "data/games.sqlite3")
    filter_by_year("data/games.sqlite3", "1995")


if __name__ == "__main__":
    main()
