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
        #loop backwards through cars
        #lane change
        for i in range(self.mapA.r):
            for j in range(self.mapA.c - 1, 0, -1):
                if self.mapA.Matrix[i][j].hasCar():
                    self.mapA.Matrix[i][j].car.changeLane()
        #loop backwards through cars
        #speed change
        for i in range(self.mapA.r):
            for j in range(self.mapA.c - 1, 0, -1):
                if self.mapA.Matrix[i][j].hasCar():
                    self.mapA.Matrix[i][j].car.move()


        self.generator.generateCars()

        #move cars
        #random add cars to map
        #i = random.randrange(9)
        #self.mapA.Matrix[i][23] = Tile(0, Car(0, 1))
