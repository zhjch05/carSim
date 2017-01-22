import matplotlib as mpl
from matplotlib import pyplot
import numpy as np
from dt import RoadMap

class Viz():
    def __init__(self, mapA):
        self.mapA = mapA

    def get2dArray(self):
        r = self.mapA.r
        c = self.mapA.c
        rawMatrix = [[0 for x in range(c)] for y in range(r)]
        for i in range(self.mapA.r):
            for j in range(self.mapA.c):
                #print self.mapA.Matrix[i][j].isDisabled
                if self.mapA.Matrix[i][j].isDisabled == 1:
                    #print("hi")
                    rawMatrix[i][j] = -5
                elif self.mapA.Matrix[i][j].hasCar():
                    #print("car")
                    rawMatrix[i][j] = 5
                else:
                    #print("good")
                    rawMatrix[i][j] = 0
        return rawMatrix

    def show(self):
        # make a color map of fixed colofrs
        cmap = mpl.colors.ListedColormap(['red','grey','black'])
        bounds=[-6,-2,2,6]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        # tell imshow about color map so that only set colors are used
        img = pyplot.imshow(self.get2dArray(),interpolation='nearest',
                            cmap = cmap,norm=norm)

        pyplot.show()
        #
        #print self.get2dArray()
