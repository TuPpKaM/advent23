import math
from collections import defaultdict

class Node():
    def __init__(self, start, left, right) -> None:
        self.start = start
        self.left = left
        self.right = right
    
def parse(file):
    instructions = []
    nodes = defaultdict(str)
    with open(file) as input:
        for i_row, li in enumerate(input):
            line = li.strip()

            if i_row == 0:
                for char in line:
                    instructions.append(char)
            elif i_row == 1:
                pass
            else:
                start, right_ = line.split('=')
                start = start.strip()
                left, right = right_.split(',')
                left = left.lstrip().lstrip('(')
                right = right.lstrip().strip(')')
                nodes[start] = Node(start,left,right)

    return instructions, nodes

def traverse(nodes, node, instruction):
    count = 0
    for inst in instruction:
        count += 1
        if inst == 'R':
            node = nodes[node.right]
        if inst == 'L':
            node = nodes[node.left]

    return node, count

def one():
    sums = 0
    instructions , nodes = parse('d8_2.txt')

    returned = nodes['AAA']
    while returned.start != 'ZZZ':
        returned, count_ = traverse(nodes, returned, instructions)
        sums += count_

    print('one', sums)

def two():
    sums = []
    instructions , nodes = parse('d8_2.txt')

    for start, node in nodes.items():
        if start.endswith('A'):
            count = 0
            returned = node
            while not returned.start.endswith('Z'):
                returned, count_ = traverse(nodes, returned, instructions)
                count += count_
            sums.append(count)

    print('two', math.lcm(*sums))

one()
two()
