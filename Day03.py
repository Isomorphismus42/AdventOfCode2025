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
    batterie_banks = read_input(3)
    max_total_output = 0
    for battery_bank in batterie_banks:
        batteries = np.array([int(i) for i in battery_bank])
        fist_digit = np.argmax(batteries[:-1])
        second_digit = np.argmax(batteries[fist_digit + 1:])
        max_total_output += batteries[fist_digit] * 10 + batteries[fist_digit + 1:][second_digit]
    return max_total_output


def part2():
    batterie_banks = read_input(3)
    max_total_output = 0
    for battery_bank in batterie_banks:
        batteries = np.array([int(i) for i in battery_bank])
        max_index = -1
        for k in range(11, -1, -1):
            batteries = batteries[max_index + 1:]
            if k:
                max_index = np.argmax(batteries[:-k])
            else:
                max_index = np.argmax(batteries)
            max_total_output += batteries[max_index] * 10 ** k
    return max_total_output


if __name__ == "__main__":
    print(part2())
