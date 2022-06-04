from random import random


# Задание 1: генератор случайных чисел
def random_generator(p):
    r = random()
    if r < p:
        return 0
    else:
        return 1


main_board = [[2, -3],
              [-1, 2]]
