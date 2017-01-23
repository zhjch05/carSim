import random
from generator import Generator
import sys
sys.path.append("..")
from model.car import Car
from model.dt import RoadMap
from model.tile import Tile
from copy import copy, deepcopy

class Tick():
    def __init__(self, mapA):
        self.mapA = mapA
        self.generator = Generator(mapA)

    def tick(self):
        #loop backwards through cars
        #lane change
        for j in range(self.mapA.c - 1, -1, -1):
            for i in range(self.mapA.r -1, -1, -1):
                if self.mapA.Matrix[i][j].hasCar():
                    newCar = self.mapA.Matrix[i][j].car.changeLane()
                    if newCar is not None:
                        self.mapA.Matrix[i][j].car = None
                        self.mapA.Matrix[newCar.x][newCar.y].car = newCar
        #loop backwards through cars
        #speed change
        for j in range(self.mapA.c - 1, -1, -1):
            for i in range(self.mapA.r -1, -1, -1):
                if self.mapA.Matrix[i][j].hasCar():
                    newCar = self.mapA.Matrix[i][j].car.move()
                    if newCar is not None:
                        if newCar.mapA is None:#poison pill
                            print(newCar.x, newCar.y)
                            self.mapA.Matrix[newCar.x][newCar.y].car = None
                        else:
                            self.mapA.Matrix[i][j].car = None
                            self.mapA.Matrix[newCar.x][newCar.y].car = newCar

        self.generator.generateCars()

        #move cars
        #random add cars to map
        #i = random.randrange(9)
        #self.mapA.Matrix[i][23] = Tile(0, Car(0, 1))
