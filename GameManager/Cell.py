class Cell:
    def __init__(self, r, c):
        self.r = r
        self.c = c
        self.exist = True
        self.neighbors = []

    def check_neighbors(self):
        ribs = []

        for n in self.neighbors:
            ribs.append(n.exist)

        if ribs.count(True) <= 1:
            self.exist = False
        elif ribs.count(True) > 3:
            return

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
