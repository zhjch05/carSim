from tile import Tile
class roadMap:

    def __init__(self):
        self.r = 9
        self.c = 50
        self.Matrix = [[0 for x in range(self.c)] for y in range(self.r)]
        for i in range(self.r):
            for j in range(self.c):
                if i == 9 and j < 6:
                    self.Matrix[i][j] = Tile(True)
                else:
                    self.Matrix[i][j] = Tile(False)
