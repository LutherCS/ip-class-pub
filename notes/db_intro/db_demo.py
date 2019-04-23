import sys
import sqlite3


def read_file(filename: str) -> list:
    """Read zoo data from the file"""
    zoo = []
    with open(filename, "r") as data:
        for line in data:
            zoo.append(tuple(line.strip().split(", ")))
    return zoo

def main(args):
    operation = args[1]
    conn = sqlite3.connect("zoo.db")
    cur = conn.cursor()

    if operation == "create":
        filename = args[2]
        print(f"creating the database from {filename}")
        cur.execute("DROP TABLE IF EXISTS animal;")
        cur.execute("CREATE TABLE animal (id, name, age, species, location);")

        animals = read_file(filename)
        cur.executemany("INSERT INTO animal VALUES (?, ?, ?, ?, ?)", animals)

        
    elif operation == "read":
        if len(args) > 2:
            species = (args[2], )
            print(f"retrieving information on {species}")
            cur.execute("SELECT * FROM animal WHERE species=?", species)
        else:
            print(f"retrieving information on all animals")
            cur.execute("SELECT * FROM animal")
        
        result = cur.fetchall()
        print(f"{'id':5}{'name':20}{'age':5}{'species':30}{'location':10}")
        for animalid, name, age, species, location in result:
            print(f"{animalid:<5}{name:20}{age:<5}{species:30}{location:<10}")

    elif operation == "update":
        print("updating database")
        cur.execute("UPDATE animal SET age = age + 1;")

    elif operation == "delete":
        species = (args[2], )
        print(f"deleting information on {species}")
        cur.execute("DELETE FROM animal WHERE species=?", species)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main(sys.argv)
