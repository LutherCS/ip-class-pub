class Vehicle:
    def __init__(self, color, year, model):
        self._color = color
        self._year = year
        self._model = model

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, new_value):
        self._color = new_value

v1 = Vehicle("pink", 2023, "Kaa")
print(v1)
