from random import randint


class Match:
    def __init__(self, p1, p2):
        self.id = randint(1000, 9999)
        self.p1 = p1
        self.p2 = p2

class Cell:
    def __init__(self, type, r, c, x, y):
        self.x = x
        self.y = y
        self.r = r
        self.c = c
        self.color = None
        self.type = type
        self.exist = True
        self.neighbors = self.neighbors(x, y)

    def neighbors(self, x, y):
        return [
            [x + 1, y],  # "u_neighbor
            [x, y + 1],  # "ur_neighbor
            [x - 1, y + 1],  # br_neighbor
            [x - 1, y],  # b_neighbor
            [x - 1, y - 1],  # bl_neighbor
            [x, y - 1],  # ul_neighbor
        ]

class Table:
    def __init__(self):
        self.table = self.create_table()
        self.count = 0
        for r in range(len(self.table)):
            for c in range(len(self.table[r])):
                cell = self.table[r][c]
                x = r - 3
                y = c - 5
                if cell == 'b':
                    self.table[r][c] = Cell("border", r, c, x, y)
                elif cell == "c":
                    self.table[r][c] = Cell("cell", r, c, x, y)
                elif cell == "p":
                    self.table[r][c] = Cell("penguin", r, c, x, y)

        for r in range(len(self.table)):
            for c in range(len(self.table[r])):
                cell = self.table[r][c]
                if r < 0:
                    cell.x = abs(cell.x)
                else:
                    cell.x = -cell.x


    def create_table(self):
        return [
        # Y  -5   -4   -3   -2   -1    0    1    2    3    4    5
            ["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], # X = 3
            ["b", "b", "b", "c", "b", "c", "b", "c", "b", "b", "b"], # X = 2
            ["b", "b", "c", "c", "c", "c", "c", "c", "c", "b", "b"], # X = 1
            ["b", "c", "c", "c", "c", "p", "c", "c", "c", "c", "b"], # X = 0
            ["b", "b", "c", "c", "c", "c", "c", "c", "c", "b", "b"], # X = -1
            ["b", "b", "c", "c", "c", "c", "c", "c", "c", "b", "b"], # X = -2
            ["b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"], # X = -3
        ]

    def get_cell(self, x, y):
        for r in range(len(self.table)):
            for c in range(len(self.table[r])):
                cell: Cell = self.table[r][c]
                if cell.x == x and cell.y == y:
                    return cell

    def delete_cell(self, x, y):
        for r in range(len(self.table)):
            for c in range(len(self.table[r])):
                cell: Cell = self.table[r][c]
                if cell.x == x and cell.y == y:
                    cell.exist = False

    def get_statement(self):
        self.processing()
        for r in range(len(self.table)):
            row = []
            for c in range(len(self.table[r])):
                cell: Cell = self.table[r][c]
                row.append([cell.type, cell.exist, cell.x, cell.y])
            print(row)

    def processing(self):
        cell = self.get_cell(0, 0)
        self.check_neighbors(cell)


    def check_neighbors(self, cell:Cell):
        if cell.type == "border" or cell.exist == False:
            return
        ribs_count = 0
        ribs = []
        for n in cell.neighbors:
            neighbor:Cell = self.get_cell(n[0], n[1])
            ribs.append(neighbor.exist)
            if neighbor.exist == True:
                ribs_count += 1
        if ribs_count <= 1:
            cell.exist = False
        elif ribs_count > 3:
            return
        else:
            for i, r in enumerate(ribs):
                if r == True:
                    # 2 ribs check
                    if ribs[i + 3] == True:
                        break
                    # 3 ribs check
                    else:
                        if ((ribs[i + 2] == True and ribs[i + 4] == True)
                        or (ribs[i + 1] == True and ribs[i + 3] == True)
                        or (ribs[i + 1] == True and ribs[i + 4] == True)):
                            break
                        else:
                            cell.exist = False
                            break

        if cell.exist == False:
            for n in cell.neighbors:
                neighbor: Cell = self.get_cell(n[0], n[1])
                self.check_neighbors(neighbor)

# table = Table()
# table.create_table()
#
# table.delete_cell(1, 0)
# table.delete_cell(0, -1)
# table.delete_cell(-1, -1)
# # table.delete_cell(-1, -1)
#
# table.delete_cell(2, -2)
# table.delete_cell(1, -3)
# table.delete_cell(0, -3)
# table.delete_cell(0, -2)
# table.get_statement()