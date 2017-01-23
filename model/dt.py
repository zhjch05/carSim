from tile import Tile
class RoadMap:

    def __init__(self):
        self.r = 9
        self.c = 40
        self.Matrix = [[0 for x in range(self.c)] for y in range(self.r)]
        for i in range(self.r):
            for j in range(self.c):
                if i < 6 and j == self.c - 1:
                    self.Matrix[i][j] = Tile(1, None)
                else:
                    self.Matrix[i][j] = Tile(0, None)
