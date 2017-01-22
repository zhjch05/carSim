from car import Car
class Generator():
    def __init__(self, mapA):
        self.c = [0, 0, 0]
        self.w = [8, 6, 3]
        self.mapA = mapA

    def generateCars(self):
        for i in range(self.w.count):
            self.c[i-1]+=1
            self.c[i-1]%=self.w[i-1]
        if self.c[0] == 1:
            self.mapA.Matrix[0][0] = Car(0, 1)
            self.mapA.Matrix[1][0] = Car(0, 1)
            self.mapA.Matrix[2][0] = Car(0, 1)
        if self.c[1] == 1:
            self.mapA.Matrix[3][0] = Car(0, 1)
            self.mapA.Matrix[4][0] = Car(0, 1)
            self.mapA.Matrix[5][0] = Car(0, 1)
        if self.c[2] == 1:
            self.mapA.Matrix[6][0] = Car(1, 1)
            self.mapA.Matrix[7][0] = Car(1, 1)
            self.mapA.Matrix[8][0] = Car(1, 1)
