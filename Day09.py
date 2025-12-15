import numpy as np
# import re
# from collections import OrderedDict
# import functools
import math


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
    coordinates = [tuple(map(int, line.split(','))) for line in read_input(9)]
    areas = []
    for i, coordinate1 in enumerate(coordinates):
        for coordinate2 in coordinates[i + 1:]:
            a, b = abs(coordinate1[0] - coordinate2[0]) + 1, abs(coordinate1[1] - coordinate2[1]) + 1
            areas.append(a * b)
    return max(areas)


def part2():
    coordinates = [tuple(map(int, line.split(','))) for line in read_input(9)]
    edges = set()
    edges_x = dict()
    edges_y = dict()
    for i, coordinate1 in enumerate(coordinates):
        check = len(edges)
        for coordinate2 in coordinates[i + 1:]:
            if coordinate1[0] == coordinate2[0]:
                if coordinate1[1] > coordinate2[1]:
                    steps = coordinate1[1] - coordinate2[1]
                    edge = [(coordinate1[0], j + coordinate2[1]) for j in range(1,steps)]
                else:
                    steps = coordinate2[1] - coordinate1[1]
                    edge = [(coordinate1[0], j + coordinate1[1]) for j in range(1,steps)]
                edges = edges.union(set(edge))
                for x, y in edge:
                    if y not in edges_y:
                        edges_y[y] = [x]
                    else:
                        edges_y[y].append(x)
            elif coordinate1[1] == coordinate2[1]:
                if coordinate1[0] > coordinate2[0]:
                    steps = coordinate1[0] - coordinate2[0]
                    edge = [(j + coordinate2[0], coordinate1[1]) for j in range(1,steps)]
                else:
                    steps = coordinate2[0] - coordinate1[0]
                    edge = [(j + coordinate1[0], coordinate1[1]) for j in range(1,steps)]
                edges = edges.union(set(edge))
                for x, y in edge:
                    if x not in edges_x:
                        edges_x[x] = [y]
                    else:
                        edges_x[x].append(y)
        if len(edges) == check:
            break
    # debug_grid = np.full((9,14), '.')
    # rows, cols = zip(*edges)
    # debug_grid[cols, rows] = 'X'
    # rows, cols = zip(*coordinates)
    # debug_grid[cols, rows] = '#'
    # print(debug_grid)

    areas = []
    for i, coordinate1 in enumerate(coordinates):
        for coordinate2 in coordinates[i + 1:]:
            a, b = coordinate1[0] - coordinate2[0] , coordinate1[1] - coordinate2[1]
            # horizontal edges check
            low_x = min(coordinate1[0], coordinate2[0])
            high_x = max(coordinate1[0], coordinate2[0])
            low_y = min(coordinate1[1], coordinate2[1])
            high_y = max(coordinate1[1], coordinate2[1])
            valid = True
            for k in range(low_x + 1, high_x):
                bounds_list = edges_x[k]
                # check if edge inbetween
                for bndry in bounds_list:
                    if low_y < bndry < high_y:
                        valid = False
                        break
                if not valid:
                    break
            if not valid:
                continue
            # vertical edges check
            for k in range(low_y + 1, high_y):
                bounds_list = edges_y[k]
                # check if edge inbetween
                for bndry in bounds_list:
                    if low_x < bndry < high_x:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                areas.append((abs(a) + 1) * (abs(b) + 1))
    return max(areas)


if __name__ == "__main__":
    print(part2())
