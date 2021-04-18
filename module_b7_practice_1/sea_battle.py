# 1. Суть написанного приложения — игра «Морской бой».
# 2. Интерфейс приложения должен представлять из себя консольное окно с двумя полями 6х6 вида:
#   | 1 | 2 | 3 | 4 | 5 | 6 |

# 1 | О | О | О | О | О | О |

# 2 | О | О | О | О | О | О |

# 3 | О | О | О | О | О | О |

# 4 | О | О | О | О | О | О |

# 5 | О | О | О | О | О | О |

# 6 | О | О | О | О | О | О |

# 3. Игрок играет с компьютером. Компьютер делает ходы наугад, но не ходит по тем клеткам, в которые он уже сходил.
# 4. Для представления корабля опишите класс Ship с конструктором принимающим в себя набор точек (координат) на игровой доске.
# 5. Опишите класс доски. Доска должна принимать в конструкторе набор кораблей.
# 6. Корабли должны находится на расстоянии минимум одна клетка друг от друга.
# 7. Корабли на доске должны отображаться следующим образом (пример):
#   | 1 | 2 | 3 | 4 | 5 | 6 |

# 1 | ■ | ■ | ■ | О | О | О |

# 2 | О | О | О | О | ■ | ■ |

# 3 | О | О | О | О | О | О |

# 4 | ■ | О | ■ | О | ■ | О |

# 5 | О | О | О | О | ■ | О |

# 6 | ■ | О | ■ | О | О | О |

# 8. На каждой доске (у ИИ и у игрока) должно находится следующее количество кораблей: 1 корабль на 3 клетки, 2 корабля на 2 клетки, 4 корабля на одну клетку.
# 9. Запретите игроку стрелять в одну и ту же клетку несколько раз. При ошибках хода игрока должно возникать исключение.
#   | 1 | 2 | 3 | 4 | 5 | 6 |

# 1 | X | X | X | О | О | О |

# 2 | О | О | О | X | X | О |

# 3 | О | T | О | О | О | О |

# 4 | ■ | О | ■ | О | ■ | О |

# 5 | О | О | О | О | ■ | О |

# 6 | ■ | О | ■ | О | О | О |

# 10. В случае, если возникают непредвиденные ситуации, выбрасывать и обрабатывать исключения.
# Буквой X помечаются подбитые корабли, буквой T — промахи.

# 11. Побеждает тот, кто быстрее всех разгромит корабли противника.

from random import randint
from exceptions import *
from inner_logic import *
from outer_logic import *


class Game:
    def __init__(self, size=6):
        self.size = size
        pl = self.random_board()
        co = self.random_board()
        co.hidden = True

        self.ai = AI(co, pl)
        self.us = User(pl, co)

    def random_board(self):
        board = None
        while board is None:
            board = self.random_place()
        return board

    def random_place(self):
        lens = [3, 2, 2, 1, 1, 1, 1]
        board = Board(size=self.size)
        attempts = 0
        for l in lens:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(
                    Dot(randint(0, self.size), randint(0, self.size)),
                    l,
                    randint(0, 1),
                )
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def greet(self):
        print("-------------------")
        print("  Приветсвуем вас  ")
        print("      в игре       ")
        print("    морской бой    ")
        print("-------------------")
        print(" формат ввода: x y ")
        print(" x - номер строки  ")
        print(" y - номер столбца ")

    def draw_board(self, user_board, ai_board):
        print("-" * 60)
        print("Доска пользователя:" + " " * 11 + "|" + "Доска компьютера:")
        for _ in range(user_board.size):
            print(user_board[_] + " | " + ai_board[_])

    def loop(self):
        num = 0
        while True:
            self.draw_board(self.us.board, self.ai.board)
            # print("-" * 20)
            # print("Доска пользователя:")
            # print(type(self.us.board))
            # print(self.us.board)
            # print("-" * 20)
            # print("Доска компьютера:")
            # print(type(self.ai.board))
            # print(self.ai.board)
            if num % 2 == 0:
                print("-" * 20)
                print("Ходит пользователь!")
                repeat = self.us.move()
            else:
                print("-" * 20)
                print("Ходит компьютер!")
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.count == 7:
                print("-" * 20)
                print("Пользователь выиграл!")
                break

            if self.us.board.count == 7:
                print("-" * 20)
                print("Компьютер выиграл!")
                break
            num += 1

    def start(self):
        self.greet()
        self.loop()


g = Game()
g.start()