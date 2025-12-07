import numpy as np
# import re
# from collections import OrderedDict
import functools
# import math


def read_input(day: int, test: bool = False):
    if test:
        path = "inputs/test_day" + str(day) + ".txt"
        print("running on test input day " + str(day))
    else:
        path = "inputs/day" + str(day) + ".txt"
        print("running day " + str(day))
    with open(path, "r") as file:
        return file.read().strip().splitlines()


def part1():
    tachyon_manifold = np.array([list(line) for line in read_input(7)])
    tachyon_manifold = np.pad(tachyon_manifold, ((0, 1), (0, 0)), 'constant', constant_values=('', 'E'))

    def step_part1(index):
        if tachyon_manifold[*index] == '.':
            tachyon_manifold[*index] = '|'
            return step_part1(index + [1, 0])
        elif tachyon_manifold[*index] == '^':
            return step_part1(index + [1, -1]) + step_part1(index + [1, 1]) + 1
        else:
            return 0

    start = np.argwhere(tachyon_manifold == 'S')[0]
    return step_part1(start + [1, 0])


def part2():
    tachyon_manifold = np.array([list(line) for line in read_input(7)])
    tachyon_manifold = np.pad(tachyon_manifold, ((0, 1), (0, 0)), 'constant', constant_values=('', 'E'))

    @functools.cache
    def step_part2(x, y):
        if tachyon_manifold[x, y] == '.':
            return step_part2(x + 1, y)
        elif tachyon_manifold[x, y] == '^':
            return step_part2(x + 1, y - 1) + step_part2(x + 1, y + 1)
        else:
            return 1

    start = np.argwhere(tachyon_manifold == 'S')[0]
    return step_part2(start[0] + 1, start[1])


if __name__ == "__main__":
    print(part2())
