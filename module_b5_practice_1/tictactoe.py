# 1. Суть написанного приложения - игра "Крестики Нолики".
# 2. Игровое поле представляет собой поле 3х3.
#   | 1 | 2 | 3 |

# 1 | О | О | О |

# 2 | О | О | О |

# 3 | О | О | О |

# 3. Игроки поочередно делают ходы.
# 4. При попытке указать точку за пределами поля, уже занятую, и при прочих исключениях предложить повторить ход.
# 5. Игра заканчивается победой одного из игроков или в случае ничьей.


def game():
    play_field = [
        ["   ", " 1 ", " 2 ", " 3 "],
        [" 1 ", " - ", " - ", " - "],
        [" 2 ", " - ", " - ", " - "],
        [" 3 ", " - ", " - ", " - "],
    ]

    show_field(play_field)

    for turn_count in range(10):
        if turn_count == 9:
            print("Ничья!")
            break
        marker = " X " if turn_count % 2 == 0 else " Y "

        coord_x, coord_y = users_input(play_field, marker)
        play_field[coord_x][coord_y] = marker

        show_field(play_field)

        if is_win(play_field, marker):
            print(f"Игрок{marker}Выиграл!\nПоздравляем!")
            break


def show_field(field):
    for row in field:
        print("".join([str(elem) for elem in row]))


def users_input(field, marker):
    while True:
        place = input(f"Введите координаты для{marker}: ").split()
        if len(place) != 2:
            print("Введите 2 координаты")
            continue

        try:
            coord_x, coord_y = int(place[0]), int(place[1])
        except ValueError:
            print("Введите два числа")
            continue

        if not (coord_x > 0 and coord_x < 4 and coord_y > 0 and coord_y < 4):
            print("Вышли за рамки поля")
            continue

        if field[coord_x][coord_y] != " - ":
            print("Клетка занята")
            continue

        break

    return coord_x, coord_y


def is_win(field, marker):
    def check_line(item_1, item_2, item_3, marker):
        if item_1 == item_2 == item_3 == marker:
            return True
        return False

    if check_line(field[1][1], field[2][2], field[3][3], marker) or check_line(
        field[3][1], field[2][2], field[1][3], marker
    ):
        return True

    for _ in range(1, 4):
        if check_line(field[_][1], field[_][2], field[_][3], marker) or check_line(
            field[1][_], field[2][_], field[3][_], marker
        ):
            return True
    return False


if __name__ == "__main__":
    game()
