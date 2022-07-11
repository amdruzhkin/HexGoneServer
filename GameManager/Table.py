from Cell import *

class Table:
    def __init__(self):
        self.statement = []
        self._statement()

    def _statement(self):
        statement = [
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
        for r in range(len(statement)):
            for c in range(len(statement[r])):
                cell = statement[r][c]
                if cell == 'b':
                    statement[r][c] = BorderCell(r, c)
                if cell == 'c':
                    statement[r][c] = PlayableCell(r, c)
                if cell == 'm':
                    statement[r][c] = MainCell(r, c)

        self.statement = statement

        for row in self.statement:
            for cell in row:
                if not isinstance(cell, BorderCell):
                    self._assign_neighbors(cell)

        # return statement

    def _assign_neighbors(self, cell):
        position = [
            [cell.r - 1, cell.c],  # "u_neighbor
            [cell.r, cell.c + 1],  # "ur_neighbor
            [cell.r + 1, cell.c + 1],  # br_neighbor
            [cell.r + 1, cell.c],  # b_neighbor
            [cell.r + 1, cell.c - 1],  # bl_neighbor
            [cell.r, cell.c + 1],  # ul_neighbor
        ]
        for p in position:
            cell.neighbors.append(self._get_cell(p[0], p[1]))


    def _get_cell(self, r, c):
        for row in self.statement:
            for cell in row:
                if cell.r == r and cell.c == c:
                    return cell

    def remove_cell(self, r, c):
        cell = self._get_cell(r, c)
        cell.exist = False
        cell.check_neighbors()

    # def check_neighbors(self, cell):
    #     if isinstance(cell, BorderCell):
    #         return
    #     if isinstance(cell, MainCell):
    #         print("")
    #
    #     ribs = []
    #     for neighbor in cell.neighbors:
    #         ribs.append(self._get_cell(neighbor[0], neighbor[1]).exist)
    #
    #     if ribs.count(True) <= 1:
    #         cell.exist = False
    #     elif ribs.count(True) > 3:
    #         return
    #     else:
    #         for i, rib in enumerate(ribs):
    #             if rib == True:
    #                 if ribs[i + 3] == True:  # 2 Ribs check
    #                     break
    #                 else:  # 3 Ribs check
    #                     if ribs[i + 2] == True and ribs[i + 4] == True:
    #                         break
    #                     elif ribs[i + 1] == True and ribs[i + 3] == True:
    #                         break
    #                     elif ribs[i + 1] == True and ribs[i + 4] == True:
    #                         break
    #                     else:
    #                         cell.exist = False
    #                         break
    #
    #     if cell.exist == False:
    #         for neighbor in cell.neighbors:
    #             self.check_neighbors(self._get_cell(neighbor[0], neighbor[1]))