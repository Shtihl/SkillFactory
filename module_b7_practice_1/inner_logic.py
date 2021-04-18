from exceptions import *


class Dot:
    def __init__(self, coord_x, coord_y):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __eq__(self, other):
        eq = self.coord_x == other.coord_x and self.coord_y == other.coord_y
        return eq

    def __repr__(self):
        return f"({self.coord_x}, {self.coord_y})"


class Ship:
    def __init__(self, bow, length, order):
        self.bow = bow
        self.length = length
        self.order = order
        self.lives = length

    @property
    def dots(self):
        ship_dots = []
        for i in range(self.length):
            current_x = self.bow.coord_x
            current_y = self.bow.coord_y

            if self.order == 0:
                current_x += i
            if self.order == 1:
                current_y += i

            ship_dots.append(Dot(current_x, current_y))

        return ship_dots

    def shooten(self, shot):
        return shot in self.dots


class Board:
    def __init__(self, hidden=False, size=6):
        self.size = size
        self.hidden = hidden

        self.count = 0

        self.field = [["0"] * size for _ in range(size)]
        self.busy = []
        self.ships = []

    def add_ship(self, ship):

        for dot in ship.dots:
            if self.out(dot) or dot in self.busy:
                raise BoardWrongShipException()
        for dot in ship.dots:
            self.field[dot.coord_x][dot.coord_y] = "■"
            self.busy.append(dot)

        self.ships.append(ship)
        self.contour(ship)

    def contour(self, ship, verb=False):
        near = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 0),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        for dot in ship.dots:
            for dx, dy in near:
                cur = Dot(dot.coord_x + dx, dot.coord_y + dy)
                if not (self.out(cur)) and cur not in self.busy:
                    if verb:
                        self.field[cur.coord_x][cur.coord_y] = "."
                    self.busy.append(cur)

    def __str__(self):
        res = ""
        res += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field):
            res += f"\n{i+1} | " + " | ".join(row) + " |"

        if self.hidden:
            res = res.replace("■", "0")
        return res

    def out(self, dot):
        return not ((0 <= dot.coord_x < self.size) and (0 <= dot.coord_y < self.size))

    def shot(self, dot):
        if self.out(dot):
            raise BoardOutException()

        if dot in self.busy:
            raise BoardUsedException()

        self.busy.append(dot)

        for ship in self.ships:
            if dot in ship.dots:
                ship.lives -= 1
                self.field[dot.coord_x][dot.coord_y] = "X"
                if ship.lives == 0:
                    self.count += 1
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False
                else:
                    print("Корабль ранен!")
                    return True

        self.field[dot.coord_x][dot.coord_y] = "."
        print("Мимо!")
        return False

    def begin(self):
        self.busy = []