import matplotlib as mpl
#mpl.use('TKAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
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
        self.rawMatrix = [[0 for x in range(c)] for y in range(r)]
        for i in range(self.mapA.r):
            for j in range(self.mapA.c):
                if self.mapA.Matrix[i][j].isDisabled == 1:
                    self.rawMatrix[i][j] = -5
                elif self.mapA.Matrix[i][j].hasCar():
                    self.rawMatrix[i][j] = 5
                else:
                    self.rawMatrix[i][j] = 0
        return self.rawMatrix

    def updatefig(self, *args):
        self.t.tick()
        self.rawMatrix = self.get2dArray()
        self.mat.set_data(self.rawMatrix)
        return self.mat


    def show(self):
        self.rawMatrix = self.get2dArray()
        # make a color map of fixed colors
        cmap = mpl.colors.ListedColormap(['red','grey','black'])
        bounds=[-6,-2,2,6]
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        fig, ax = plt.subplots()
        # tell imshow about color map so that only set colors are used
        self.mat = ax.matshow(self.rawMatrix,interpolation='nearest', cmap = cmap,norm=norm, animated=True)

        plt.xticks(np.arange(0, 50, 1.0))
        plt.yticks(np.arange(0, 9, 1.0))

        plt.grid(True,color='white',linewidth = 1.5 )
        #fig = plt.subplots()

        anim = animation.FuncAnimation(fig, self.updatefig, interval=500)
        plt.show()
