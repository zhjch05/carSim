class Tile:
    def __init__(self, isDisabled, car):
        self.isDisabled = isDisabled
        self.car = car

    def hasCar(self):
         return self.car is not None
