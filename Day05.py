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
    i = read_input(5)
    id_ranges = [range(int(k.split('-')[0]),int(k.split('-')[1]) + 1) for k in i[:i.index('')]]
    available_id = [int(k) for k in i[i.index('') + 1:]]
    fresh = 0
    for id in available_id:
        for id_range in id_ranges:
            if id in id_range:
                fresh += 1
                break
    return fresh


def part2():
    i = read_input(5)
    id_ranges = [[int(k.split('-')[0]),int(k.split('-')[1])] for k in i[:i.index('')]]
    id_ranges.sort(key=lambda x: x[0])
    merged_intervals = [id_ranges[0]]
    for id_range in id_ranges:
        if id_range[0] <= merged_intervals[-1][1]:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], id_range[1])
        else:
            merged_intervals.append(id_range)
    return sum([n[1] - n[0] + 1 for n in merged_intervals])


if __name__ == "__main__":
    print(part2())
