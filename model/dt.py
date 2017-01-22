from tile import Tile
class RoadMap:

    def __init__(self):
        self.r = 9
        self.c = 50
        self.Matrix = [[0 for x in range(self.c)] for y in range(self.r)]
        for i in range(self.r):
            for j in range(self.c):
                if i < 6 and j == 49:
                    self.Matrix[i][j] = Tile(1)
                else:
                    self.Matrix[i][j] = Tile(0)
