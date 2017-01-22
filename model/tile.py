class Tile:
    def __init__(self, isDisabled):
        self.isDisabled = isDisabled
        self.car = None

    def hasCar(self):
         return self.car is not None
