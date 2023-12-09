from math import lcm
from time import time_ns


start_time = time_ns()

class Node:
    def __init__(self, name, left, right):
        self.name = name
        self.left = left
        self.right = right


def parse_input(filename):
    node_directory = {}
    list_of_a = []

    with open(filename) as file:
        steps, nodes = file.read().split("\n\n")
        nodes = nodes.split('\n')
        nodes.pop()   #  remove last enter
        for node in nodes:
            parent_name, left_right = node.split(" = ")
            left, right = left_right.strip("()").split(", ")
            parent = Node(parent_name, left, right)
            node_directory[parent_name] = parent
            if parent_name[2] == "A": list_of_a.append(parent)
    return node_directory, steps, list_of_a


def steps_till_z(starting_node, nodes, steps):
    i = 0
    working_node = starting_node
    while working_node.name[2] != 'Z':
        direction = steps[i % (len(steps))]
        working_node = nodes[working_node.right] if direction == "R" else nodes[working_node.left]
        i += 1
    return i


def find_least_common_multiple(numbers):
    result = numbers[0]
    for number in numbers[1:]:
        result = lcm(result, number)
    return result


def main(filename):
    nodes, steps, list_of_nodes = parse_input(filename)
    steps_list = []
    for node in list_of_nodes:
        steps_list.append(steps_till_z(node, nodes, steps))

    answer = find_least_common_multiple(steps_list)
    print(f"The least common multiple is: {answer}")


main("Input/Day08.txt")
print("day 08")
print("--- %s ms ---" % ((time_ns() - start_time)/1000000))
