def game():
    play_field = [
        ["   ", " 1 ", " 2 ", " 3 "],
        [" 1 ", " - ", " - ", " - "],
        [" 2 ", " - ", " - ", " - "],
        [" 3 ", " - ", " - ", " - "],
    ]

    draw_field(play_field)
    mark = "X"
    make_turn()
    switch_mark(mark)
    print(mark)


def switch_mark(mark):
    possible_mark = ["X", "O"]
    if mark == possible_mark[0]:
        mark = possible_mark[1]
        return mark
    if mark == possible_mark[1]:
        mark = possible_mark[0]
        return mark


def make_turn():
    point = list(input("введите координаты через пробел").split())


def draw_field(field):
    for row in field:
        print("".join([str(elem) for elem in row]))


def is_win(field):
    win_patterns = [
        [field[1][1], field[1][2], field[1][3]],
        [field[2][1], field[2][2], field[2][3]],
        [field[3][1], field[3][2], field[3][3]],
        [field[1][1], field[2][1], field[3][1]],
        [field[1][2], field[2][2], field[3][2]],
        [field[1][3], field[2][3], field[3][3]],
        [field[1][1], field[2][2], field[3][3]],
        [field[3][1], field[2][2], field[1][3]],
    ]


if __name__ == "__main__":
    game()


# Запускаем функцию game()
# В game инициализируем поле через draw_field
# Задаём стартовый маркер
# Ждём хода игрока через make_turn

# draw_field - построчно выводим игровое поле

# make_turn - на входе принимаем маркер и поле
# получаем координаты, проверяем что корректные
# модифицируем поле, перерисовываем

# is_win ловим на вход поле, проверяем есть ли попадение в победный паттерн
