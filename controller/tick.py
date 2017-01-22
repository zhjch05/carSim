from generator import Generator
class Tick():
    def __init__(self, mapA):
        self.mapA = mapA
        self.generator = Generator(mapA)

    def tick(self):
        self.generator.generateCars()
