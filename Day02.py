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
    ID_ranges = read_input(2)[0].split(',')
    repetitive_numbers = list()
    for ID_range in ID_ranges:
        lower, upper = ID_range.split('-')
        upper = int(upper)
        k = len(lower)
        if k % 2:
            if 10 ** k <= upper:
                n = 10 ** int((k - 1) / 2)
            else:
                continue
        else:
            n = int(lower[:int(k/2)])
            if n < int(lower[int(k/2):]):
                n += 1
        while int(str(n) * 2) <= upper:
            repetitive_numbers.append(int(str(n) * 2))
            n += 1
    return sum(repetitive_numbers)


def part2():
    ID_ranges = read_input(2)[0].split(',')
    repetitive_numbers = list()
    for ID_range in ID_ranges:
        lower, upper = ID_range.split('-')
        for n in range(int(lower), int(upper) + 1):
            digits = str(n)
            d_count = len(digits)
            for i in range(int(d_count/2)):
                number = digits[:i+1] * (int(d_count / (i+1)))
                if number == digits:
                    repetitive_numbers.append(int(number))
                    break
    repetitive_numbers.append(0)
    return sum(repetitive_numbers)


if __name__ == "__main__":
    print(part2())
