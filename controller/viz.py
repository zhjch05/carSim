import matplotlib as mpl
from matplotlib import pyplot
import numpy as np
from model.dt import RoadMap
import time
from tick import Tick

class Viz():
    def __init__(self, mapA):
        self.mapA = mapA
        self.t = Tick(mapA)

    def get2dArray(self):
        r = self.mapA.r
        c = self.mapA.c
        rawMatrix = [[0 for x in range(c)] for y in range(r)]
        for i in range(self.mapA.r):
            for j in range(self.mapA.c):
                if self.mapA.Matrix[i][j].isDisabled == 1:
                    rawMatrix[i][j] = -5
                elif self.mapA.Matrix[i][j].hasCar():
                    rawMatrix[i][j] = 5
                else:
                    rawMatrix[i][j] = 0
        return rawMatrix

    def show(self):
        self.t.tick()
        rawMatrix = self.get2dArray()
        # make a color map of fixed colors
        cmap = mpl.colors.ListedColormap(['red','grey','black'])
        bounds=[-6,-2,2,6]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        # tell imshow about color map so that only set colors are used
        img = pyplot.imshow(rawMatrix,interpolation='nearest', cmap = cmap,norm=norm)
        pyplot.xticks(np.arange(0, 50, 1.0))
        pyplot.yticks(np.arange(0, 9, 1.0))

        pyplot.grid(True,color='white',linewidth = 1.5 )
        pyplot.show()
