from random import randint


class Match:
    def __init__(self, p1, p2):
        self.id = randint(1000, 9999)
        self.p1 = p1
        self.p2 = p2

