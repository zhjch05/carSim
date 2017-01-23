import random
from generator import Generator
import sys
sys.path.append("..")
from model.car import Car
from model.dt import RoadMap
from model.tile import Tile

class Tick():
    def __init__(self, mapA):
        self.mapA = mapA
        self.generator = Generator(mapA)

    def tick(self):
        self.generator.generateCars()

        #move cars
        #random add cars to map
        i = random.randrange(9)
        self.mapA.Matrix[i][23] = Tile(0, Car(0, 1))
