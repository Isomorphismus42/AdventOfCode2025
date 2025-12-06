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
    worksheet = np.array([line.split() for line in read_input(6)])
    numbers = worksheet[:-1,:].astype(int)
    grand_total = 0
    for index,  operator in enumerate(worksheet[-1,:]):
        if operator == '+':
            grand_total += np.sum(numbers[:,index])
        else:
            grand_total += np.prod(numbers[:,index])
    return grand_total


def part2():
    i = read_input(6)
    worksheet = np.array([list(line) for line in i[:-1]])
    seperator = np.full((worksheet.shape[0],1), ' ')
    worksheet = np.append(worksheet, seperator, axis=1)
    operators = i[-1].split()
    grand_total = 0
    numbers = []
    for column in worksheet.T:
        if np.array_equiv(column, seperator):
            grand_total += np.sum(numbers) if operators.pop(0) == '+' else np.prod(numbers)
            numbers.clear()
        else:
            numbers.append(int(''.join(column)))
    return grand_total


if __name__ == "__main__":
    print(part2())
