from dt import RoadMap
from tile import Tile
from copy import copy, deepcopy
class Car:
    def __init__(self, mapA, v, a, p, x, y):
        self.mapA = mapA
        self.v = v
        self.a = a
        self.p = 1
        self.x = x
        self.y = y

    def getTile(self):
        return self.mapA.Matrix[self.x][self.y]

    def getRightFrontTile(self, x, y):
        True

    def getFrontTile(self):
        if self.y + 1 > self.mapA.c - 1:
            return None
        else:
            return self.mapA.Matrix[self.x][self.y+1]

    def getRightTile(self):
        if self.x + 1 > self.mapA.r - 1:
            return None
        else:
            return self.mapA.Matrix[self.x+1][self.y]

    def getFrontCar(self):
        for i in range(self.y + 1, self.mapA.c):
            if self.mapA.Matrix[self.x][i].hasCar():
                return self.mapA.Matrix[self.x][i].car
        return None

    def getRightCar(self):
        if self.getRightTile() is not None:
            return self.getRightTile().car
        return None

    def getRightFrontCar(self):
        if self.x + 1 > self.mapA.r - 1:
            return None
        for i in range(self.y + 1, self.mapA.c):
            if self.mapA.Matrix[self.x+1][i].hasCar():
                return self.mapA.Matrix[self.x+1][i].car
        return None

    def getRightRearCar(self):
        if self.x + 1 > self.mapA.r - 1:
            return None
        for i in range(self.y - 1, -1):
            if self.mapA.Matrix[self.x+1][i].hasCar():
                return self.mapA.Matrix[self.x+1][i].car
        return None

    def horizDistance(self, frontCar):
        return frontCar.y - self.y - 1

    def stepForward(self):
        tempY = self.y
        for i in range(0, self.v):
            frontTile = self.getFrontTile()
            if frontTile is None:
                print("Car successfully exits!")
                return Car(None, 0, 0, 0, self.x, tempY) #poison pill to let tick remove this car from roadmap
            elif frontTile.isDisabled == 1:
                return Car(self.mapA, 0, self.a, self.p, self.x, self.y)
            else:
                self.y+=1
        return Car(self.mapA, self.v, self.a, self.p, self.x, self.y)
        #
        # if self.v + self.y > self.mapA.c - 1:
        #     if self.x < 6:
        #         return Car(self.mapA, 0, self.a, self.p, self.x, self.mapA.c - 2)
        #     else:
        #         return Car(None, 0, 0, 0, self.x, self.y) #poison pill to let tick remove this car from roadmap
        #         print("Car successfully exits!")
        # elif self.v + self.y == self.mapA.c - 1:
        #     if self.x < 6:
        #         return Car(self.mapA, 0, self.a, self.p, self.x, self.mapA.c - 2)
        #     else:
        #         return Car(self.mapA, self.v, self.a, self.p, self.x, self.y + self.v)
        # else:
        #     return Car(self.mapA, self.v, self.a, self.p, self.x, self.y + self.v)


    # def changeLane(self):
    #     frontTile = self.getFrontTile()
    #     if frontTile is not None:
    #         if frontTile.isDisabled == 1:
    #             rightTile = self.getRightTile()
    #             if rightTile is not None:
    #                 if not rightTile.hasCar():
    #                     return Car(self.mapA, self.v, self.a, self.p, self.x + 1, self.y)

    def changeLane(self):
        frontTile = self.getFrontTile()
        if frontTile is not None:
            if frontTile.isDisabled == 1:
                rightTile = self.getRightTile()
                if rightTile is not None:
                    if not rightTile.hasCar():
                        return Car(self.mapA, self.v, self.a, self.p, self.x + 1, self.y)
        rightFrontCar = self.getRightFrontCar()
        rightRearCar = self.getRightRearCar()
        rightCar = self.getRightCar()
        if rightRearCar is not None:
            if self.v > rightRearCar.v:
                if rightFrontCar is not None:
                    if self.v <= rightFrontCar.v:
                        if rightCar is None:
                            if self.x < 8:
                                return Car(self.mapA, self.v, self.a, self.p, self.x + 1, self.y)
                else:
                    if rightCar is None:
                        if self.x < 8:
                            return Car(self.mapA, self.v, self.a, self.p, self.x + 1, self.y)
        else:
            if rightFrontCar is not None:
                if self.v <= rightFrontCar.v:
                    if rightCar is None:
                        if self.x < 8:
                            return Car(self.mapA, self.v, self.a, self.p, self.x + 1, self.y)
            else:
                if rightCar is None:
                    if self.x < 8:
                        return Car(self.mapA, self.v, self.a, self.p, self.x + 1, self.y)

    def move(self):
        frontCar = self.getFrontCar()
        if frontCar is not None:
            dis = self.horizDistance(frontCar)
            if self.v > dis:
                print("Car at ",self.x,self.y," brakes ",self.v-dis)
                self.v = dis
            else:
                self.v+=self.a
                if self.v > dis:
                    print("Car at ",self.x,self.y," brakes ",self.v-dis)
                    self.v = dis
        else:
             self.v+=self.a
        return self.stepForward()
