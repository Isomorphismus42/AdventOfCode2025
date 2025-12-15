import numpy as np
from scipy import optimize
# import re
# from collections import OrderedDict
# import functools
import math

from scipy.optimize import LinearConstraint


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
    machines = read_input(10)
    fewest_total_presses = 0

    for machine in machines:
        light_diagram = machine[1:].split(']')[0].replace('.','0').replace('#', '1')
        digits = len(light_diagram)
        bin_light_diagram = int(light_diagram, 2)
        buttons = machine.strip().split(' ')[1:-1]
        bin_buttons = set()
        for button in buttons:
            button = button[1:-1].replace(',', '')
            bin_button = ['0'] * digits
            for s in button:
                bin_button[int(s)] = '1'
            bin_button = int(''.join(bin_button),2)
            bin_buttons.add(bin_button)
        stack = [bin_light_diagram]
        visited = {bin_light_diagram}
        found = False
        for depth in range(digits):
            new_stack = []
            while stack and not found:
                state = stack.pop(0)
                for button in bin_buttons:
                    next_state = state ^ button
                    if next_state == 0:
                        found = True
                        break
                    elif next_state not in visited:
                        new_stack.append(next_state)
                        visited.add(next_state)
            if found:
                fewest_total_presses += depth + 1
                break
            stack = new_stack
    return fewest_total_presses


def part2():
    machines = read_input(10)
    fewest_total_presses = 0
    for machine in machines:
        joltage_requirements = machine.split('{')[1][:-1]
        joltage_requirements = np.array([int(i) for i in joltage_requirements.split(',')])
        buttons = machine.strip().split(' ')[1:-1]
        bin_buttons = []
        for button in buttons:
            button = button[1:-1].replace(',', '')
            bin_button = ['0'] * joltage_requirements.shape[0]
            for s in button:
                bin_button[int(s)] = '1'
            bin_buttons.append(bin_button)
        bin_buttons = np.array(bin_buttons).astype(int)
        # print(np.linalg.lstsq(bin_buttons.T, joltage_requirements, rcond=None)[0])
        c = np.ones(bin_buttons.shape[0])
        fewest_total_presses += optimize.milp(c, integrality=c, constraints=LinearConstraint(bin_buttons.T, joltage_requirements, joltage_requirements)).fun
    return int(fewest_total_presses)


if __name__ == "__main__":
    print(part2())
