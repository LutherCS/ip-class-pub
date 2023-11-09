#!/usr/bin/env python3
"""Working with PostgreSQL"""

import psycopg


def main():
    """Main"""
    with psycopg.connect(
        host="knuth.luther.edu", port=5432, dbname="world", user="username"
    ) as conn:
        with conn.cursor() as cur:
            cur.execute("select * from country limit 10")
            rows = cur.fetchall()
            print(rows)


if __name__ == "__main__":
    main()
