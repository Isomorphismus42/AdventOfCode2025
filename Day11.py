
# import numpy as np
# import re
# from collections import OrderedDict
import functools
# import math

from scipy.optimize import LinearConstraint


def read_input(day: int, test: bool = False):
    if test:
        path = "inputs/test_day" + str(day) + "p2.txt"
        print("running on test input day " + str(day))
    else:
        path = "inputs/day" + str(day) + ".txt"
        print("running day " + str(day))
    with open(path, "r") as file:
        return file.read().strip().splitlines()


def part1():
    server_rack = dict()
    for line in read_input(11):
        line = line.split(' ')
        server_rack[line[0][:-1]] = line[1:]
    stack = ['you']
    paths_count = 0
    while stack:
        server_in = stack.pop(0)
        server_out = server_rack[server_in]
        for s in server_out:
            if s == 'out':
                paths_count += 1
            else:
                stack.append(s)
    return paths_count


def part2():
    server_rack = dict()
    for line in read_input(11):
        line = line.split(' ')
        server_rack[line[0][:-1]] = line[1:]

    @functools.cache
    def resolve(server_in,dac,fft):
        if server_in == 'out':
            if dac and fft:
                return 1
            else:
                return 0

        if server_in == 'dac':
            dac = True
        elif server_in == 'fft':
            fft = True

        server_out = server_rack[server_in]
        paths = 0
        for s in server_out:
            paths += resolve(s,dac,fft)
        return paths
    return resolve('svr', False, False)


if __name__ == "__main__":
    print(part2())
