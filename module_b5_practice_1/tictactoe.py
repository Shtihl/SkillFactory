def game():
    play_field = [
        ["   ", " 1 ", " 2 ", " 3 "],
        [" 1 ", " - ", " - ", " - "],
        [" 2 ", " - ", " - ", " - "],
        [" 3 ", " - ", " - ", " - "],
    ]

    show_field(play_field)

    turn_count = 0

    for turn_count in range(10):
        if turn_count == 9:
            print("Ничья!")
            break
        if turn_count % 2 == 0:
            marker = " X "
        else:
            marker = " Y "

        coord_x, coord_y = users_input(play_field, marker)
        play_field[coord_x][coord_y] = marker

        if is_win(play_field, marker):
            print(f"Player{marker} win")
            show_field(play_field)
            break
        else:
            show_field(play_field)


def show_field(field):
    for row in field:
        print("".join([str(elem) for elem in row]))


def users_input(field, marker):
    while True:
        place = input(f"Input coordinates for mark{marker}: ").split()
        if len(place) != 2:
            print("Input two coordinates")
            continue
        if not (place[0].isdigit() and place[1].isdigit()):
            print("Input numbers")
            continue
        coord_x, coord_y = map(int, place)
        if not (coord_x > 0 and coord_x < 4 and coord_y > 0 and coord_y < 4):
            print("Out of indexes")
            continue
        if field[coord_x][coord_y] != " - ":
            print("Cell not empty")
            continue
        break
    return coord_x, coord_y


def is_win(field, marker):
    def check_line(item_1, item_2, item_3, marker):
        if item_1 == item_2 == item_3 == marker:
            return True
        return False

    for _ in range(1, 4):
        if (
            check_line(field[_][1], field[_][2], field[_][3], marker)
            or check_line(field[1][_], field[2][_], field[3][_], marker)
            or check_line(field[1][1], field[2][2], field[3][3], marker)
            or check_line(field[3][1], field[2][2], field[1][3], marker)
        ):
            return True
    return False


if __name__ == "__main__":
    game()
