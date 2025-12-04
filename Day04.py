from itertools import count

import numpy as np
# import re
# from collections import OrderedDict
# import functools
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
    grid = np.array([list(line) for line in read_input(4)])
    grid_pad = np.pad(grid, ((1,1),(1,1)), 'constant', constant_values=('.', '.'))
    can_be_accessed = 0
    for idx, x in np.ndenumerate(grid):
        if x == '@':
            neighbours = 0
            for i in range(3):
                for j in range(3):
                    if grid_pad[i + idx[0],j + idx[1]] == '@' and (i, j) != (1,1):
                        neighbours += 1
            if neighbours < 4:
                can_be_accessed += 1
    return can_be_accessed


def part2():
    grid = np.array([list(line) for line in read_input(4)])
    grid_pad = np.pad(grid, ((1,1),(1,1)), 'constant', constant_values=('.', '.'))
    can_be_accessed = 0
    can_be_accessed_prev = -1
    while can_be_accessed_prev != can_be_accessed:
        can_be_accessed_prev = can_be_accessed
        for idx, x in np.ndenumerate(grid_pad[1:-1, 1:-1]):
            if x == '@':
                neighbours = 0
                for i in range(3):
                    for j in range(3):
                        if grid_pad[i + idx[0],j + idx[1]] == '@' and (i, j) != (1,1):
                            neighbours += 1
                if neighbours < 4:
                    can_be_accessed += 1
                    grid_pad[idx[0] + 1, idx[1] + 1] = '.'
    return can_be_accessed


if __name__ == "__main__":
    print(part2())
