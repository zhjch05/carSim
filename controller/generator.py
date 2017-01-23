import sys
sys.path.append("..")
from model.car import Car
from model.dt import RoadMap
from model.tile import Tile


class Generator():
    def __init__(self, mapA):
        self.c = [0, 0, 0]
        self.w = [8, 6, 3]
        self.mapA = mapA

    def generateCars(self):
        for i in range(len(self.w)):
            self.c[i-1]+=1
            self.c[i-1]%=self.w[i-1]
        if self.c[0] == 1:
            for i in range(0,3):
                if self.mapA.Matrix[i][0].hasCar():
                    print("cannot accommodate more cars!")
                    #sys.exit("cannot accommodate more cars!")
                else:
                    self.mapA.Matrix[i][0] = Tile(0, Car(self.mapA, 0, 1, 1, i, 0))
        if self.c[1] == 1:
            for i in range(3,6):
                if self.mapA.Matrix[i][0].hasCar():
                    print("cannot accommodate more cars!")
                    #sys.exit("cannot accommodate more cars!")
                else:
                    self.mapA.Matrix[i][0] = Tile(0, Car(self.mapA, 0, 1, 1, i, 0))
        if self.c[2] == 1:
            for i in range(6,9):
                if self.mapA.Matrix[i][0].hasCar():
                    print("cannot accommodate more cars!")
                    #sys.exit("cannot accommodate more cars!")
                else:
                    self.mapA.Matrix[i][0] = Tile(0, Car(self.mapA, 1, 1, 1, i, 0))
        return self.mapA.Matrix
