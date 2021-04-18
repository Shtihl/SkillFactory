from random import randint
from exceptions import *
from inner_logic import Dot


class Player:
    def __init__(self, board, enemy):
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        dot = Dot(randint(0, 5), randint(0, 5))
        print(f"Ход компьютера: {dot.coord_x+1} {dot.coord_y+1}")
        return dot


class User(Player):
    def ask(self):
        while True:
            cords = input("Ваш ход: ").split()

            if len(cords) != 2:
                print(" Введите 2 координаты! ")
                continue

            coord_x, coord_y = cords

            if not (coord_x.isdigit()) or not (coord_y.isdigit()):
                print(" Введите числа! ")
                continue

            coord_x, coord_y = int(coord_x), int(coord_y)

            return Dot(coord_x - 1, coord_y - 1)
