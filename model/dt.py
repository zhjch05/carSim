from tile import Tile
class RoadMap:

    def __init__(self):
        self.r = 9
        self.c = 30
        self.Matrix = [[0 for x in range(self.c)] for y in range(self.r)]
        for i in range(self.r):
            for j in range(self.c):
                # if i < 6 and j == self.c - 1:
                #     self.Matrix[i][j] = Tile(1, None)
                # else:
                self.Matrix[i][j] = Tile(0, None)

        for j in range(20, 30):
            self.Matrix[0][j] = Tile(1, None)
        for j in range(22, 30):
            self.Matrix[1][j] = Tile(1, None)
        for j in range(24, 30):
            self.Matrix[2][j] = Tile(1, None)
        for j in range(26, 30):
            self.Matrix[3][j] = Tile(1, None)
        for j in range(27, 30):
            self.Matrix[4][j] = Tile(1, None)
        for j in range(28, 30):
            self.Matrix[5][j] = Tile(1, None)
