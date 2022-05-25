from typing import List
from math import log2, ceil

class Node:
    def __init__(self, val=0):
        self.val = val
        self.predecessors = []

def second_smallest_element(a: List[Node]):
    logn = ceil(log2(len(a)))
    for _ in range(logn):
        l = []
        for i in range(0, len(a) - 1, 2):
            if a[i].val <= a[i + 1].val:
                a[i].predecessors.append(a[i + 1].val)
                l.append(a[i])
            else:
                a[i + 1].predecessors.append(a[i].val)
                l.append(a[i + 1])
        if len(a) % 2: l.append(a[-1])
        a = l
    firstNode = a[0]
    first = firstNode.val
    second = min(firstNode.predecessors)
    return first, second

if __name__ == '__main__':
    print(second_smallest_element([Node(3), Node(5), Node(8), Node(4), Node(1), Node(9)]))
