from operator import index

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
    coordinates = [tuple(map(int, line.split(','))) for line in read_input(8)]
    n = len(coordinates)
    routing_table = np.zeros((n, n)) # will have 0s on the diagonal
    for i, coordinate1 in enumerate(coordinates):
        for j, coordinate2 in enumerate(coordinates):
            euklid_distance = (math.dist(coordinate1, coordinate2))
            routing_table[i][j] = euklid_distance
    idx_sorted = np.argsort(routing_table, axis=None) # flattened index list sorted by value
    idx_2d_sorted = np.unravel_index(idx_sorted, routing_table.shape) # transform back into 2d coordinates

    circuit_list = list()
    connections = 1000
    for counter in range(n, n + connections*2, 2): # start at n to avoid 0s and do 2 steps because routing_table is symmetric
        junction_box1 = int(idx_2d_sorted[0][counter])
        junction_box2 = int(idx_2d_sorted[1][counter])
        circuit1 = set()
        circuit2 = set()
        for circuit in circuit_list:
            if junction_box1 in circuit and junction_box2 in circuit:
                break
            if junction_box1 in circuit:
                circuit1 = circuit
            if junction_box2 in circuit:
                circuit2 = circuit
        else:
            if circuit1 and circuit2:
                circuit_list.append(circuit1.union(circuit2))
                circuit_list.remove(circuit1)
                circuit_list.remove(circuit2)
            elif circuit1:
                circuit1.add(junction_box2)
            elif circuit2:
                circuit2.add(junction_box1)
            else:
                circuit_list.append({junction_box1, junction_box2})
    circuit_lengths = [len(circuit) for circuit in circuit_list]
    circuit_lengths.sort(reverse=True)
    return math.prod(circuit_lengths[:3])


def part2():
    coordinates = [tuple(map(int, line.split(','))) for line in read_input(8)]
    n = len(coordinates)
    routing_table = np.zeros((n, n)) # will have 0s on the diagonal
    for i, coordinate1 in enumerate(coordinates):
        for j, coordinate2 in enumerate(coordinates):
            euklid_distance = (math.dist(coordinate1, coordinate2))
            routing_table[i][j] = euklid_distance
    idx_sorted = np.argsort(routing_table, axis=None)  # flattened index list sorted by value
    idx_2d_sorted = np.unravel_index(idx_sorted, routing_table.shape)  # transform back into 2d coordinates


    circuit_list = list()
    for counter in range(n, n ** 2, 2):  # start at n to avoid 0s and do 2 steps because routing_table is symmetric
        junction_box1 = int(idx_2d_sorted[0][counter])
        junction_box2 = int(idx_2d_sorted[1][counter])
        circuit1 = set()
        circuit2 = set()
        for circuit in circuit_list:
            if junction_box1 in circuit and junction_box2 in circuit:
                break
            if junction_box1 in circuit:
                circuit1 = circuit
            if junction_box2 in circuit:
                circuit2 = circuit
        else:
            if circuit1 and circuit2:
                circuit_list.append(circuit1.union(circuit2))
                circuit_list.remove(circuit1)
                circuit_list.remove(circuit2)
            elif circuit1:
                circuit1.add(junction_box2)
            elif circuit2:
                circuit2.add(junction_box1)
            else:
                circuit_list.append({junction_box1, junction_box2})
        if len(circuit_list[0]) == n:
            return coordinates[junction_box1][0] * coordinates[junction_box2][0]
    return 0


if __name__ == "__main__":
    print(part2())
