"""OOP in Python"""


class Game:
    def __init__(self, title, designer):
        self._title = title
        self._designer = designer

    def __str__(self) -> str:
        return f"{self._title} by {self._designer}"

    def get_title(self):
        return self._title

    def set_title(self, new_value):
        self._title = new_value

    title = property(get_title, set_title)


class Library:
    def __init__(self):
        self._collection = []
        self.index = -1

    def add(self, new_game):
        self._collection.append(new_game)

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index < len(self._collection):
            return self._collection[self.index]
        raise StopIteration

    def __len__(self):
        return len(self._collection)


a_game = Game("Pandemic", "Matt Leacock")
b_game = Game("Ticket to Ride", "Alan Moon")
print(a_game)
print(str(a_game))
print(a_game._title)
print(a_game.title)
a_game.title = "Ticket to Ride"
print(a_game.title)
my_games = Library()
my_games.add(a_game)
my_games.add(b_game)
print(my_games)
print(f"There are {len(my_games)} games in my collection")
for game in my_games:
    print(game)
