# import numpy as np
# import re
# from collections import OrderedDict
# import functools
# import math


def read_input(day: int, test: bool = False):
    if test:
        path = "inputs/test_day" + str(day) + ".txt"
        print("running on test input")
    else:
        path = "inputs/day" + str(day) + ".txt"
    with open(path, "r") as file:
        return file.read().strip().splitlines()


def part1():
    lines = read_input(day=1)
    position = 50
    count = 0
    for line in lines:
        if line[0] == 'L':
            position -= int(line[1:].strip())
        else:
            position += int(line[1:].strip())
        position %= 100
        if position == 0:
            count += 1
    return count


def part2():
    lines = read_input(day=1)
    position = 50
    count = 0
    for line in lines:
        prev_count = count
        if line[0] == 'L':
            if position == 0:
                count -= 1
            position -= int(line[1:].strip())
            if position <= 0:
                count += 1 + abs(int(position / 100))
        else:
            position += int(line[1:].strip())
            count += int(position / 100)
        position %= 100
    return count


if __name__ == "__main__":
    print(part2())
