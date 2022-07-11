from random import randint

from Cell import MainCell
from Table import Table


class Match:
    def __init__(self, p1, p2):
        self.id = randint(1000, 9999)
        self.p1 = p1
        self.p2 = p2
        self.Table = Table()


if __name__ == "__main__":
    match = Match("p1", "p2")

    match.Table.remove_cell(3, 4)
    # match.Table.remove_cell(3, 6)
    # match.Table.remove_cell(4, 4)
    # match.Table.remove_cell(2, 5)
    # match.Table.remove_cell(4, 6)
    # match.Table.remove_cell(4, 5)

    for row in match.Table.statement:
        _row = []
        for cell in row:
            if isinstance(cell, MainCell):
                _row.append(["M", cell.exist])
            else:
                _row.append(cell.exist)
        print(_row)


