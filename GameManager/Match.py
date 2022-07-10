from random import randint

from Cell import *

class Match:
    def __init__(self, p1, p2):
        self.id = randint(1000, 9999)
        self.p1 = p1
        self.p2 = p2
        self.table = self._table()

    def _table(self):
        table = [
        # Y  -5   -4   -3   -2   -1    0    1    2    3    4    5
        # C   0    1    2    3    4    5    6    7    8    9    10
            ["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], # R = 0 X = 3
            ["b", "b", "b", "c", "b", "c", "b", "c", "b", "b", "b"], # R = 1 X = 2
            ["b", "b", "c", "c", "c", "c", "c", "c", "c", "b", "b"], # R = 2 X = 1
            ["b", "c", "c", "c", "c", "m", "c", "c", "c", "c", "b"], # R = 3 X = 0
            ["b", "b", "c", "c", "c", "c", "c", "c", "c", "b", "b"], # R = 4 X = -1
            ["b", "b", "c", "c", "c", "c", "c", "c", "c", "b", "b"], # R = 5 X = -2
            ["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], # R = 6 X = -3
        ]

        for r in range(len(table)):
            for c in range(len(table[r])):
                cell = table[r][c]
                if cell == 'b':
                    table[r][c] = BorderCell(r, c)
                if cell == 'c':
                    table[r][c] = PlayableCell(r, c)
                if cell == 'm':
                    table[r][c] = MainCell(r, c)

        return table

    def _get_cell(self, r, c):
        for row in self.table:
            for cell in row:
                if cell.r == r and cell.c == c:
                    return cell

    def remove_cell(self, r, c):
        cell = self._get_cell(r, c)
        cell.exist = False


if __name__ == "__main__":
    match = Match("p1", "p2")

    match.remove_cell(3, 4)
    match.remove_cell(3, 6)
    # match.remove_cell(0, -2)

    for r in match.table:
        row = []
        for c in r:
            if isinstance(c, MainCell):
                if c.exist == False:
                    row.append(["M", False])
                else:
                    row.append("M")
            else:
                row.append(c.exist)
        print(row)



