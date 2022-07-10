class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.exist = True
        self.neighbors = self._neighbors()

    def _neighbors(self):
        return [
            [self.r - 1, self.c],  # "u_neighbor
            [self.r, self.c + 1],  # "ur_neighbor
            [self.r + 1, self.c + 1],  # br_neighbor
            [self.r + 1, self.c],  # b_neighbor
            [self.r + 1, self.c - 1],  # bl_neighbor
            [self.r, self.c + 1],  # ul_neighbor
        ]

class PlayableCell(Cell):
    def __init__(self, r, c, color=None):
        super().__init__(r, c)
        self.color = color

class MainCell(Cell):
    def __init__(self, r, c):
        super().__init__(r, c)

class BorderCell(Cell):
    def __init__(self, r, c):
        super().__init__(r, c)
