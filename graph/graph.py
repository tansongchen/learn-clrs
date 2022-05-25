from typing import Dict, List, Tuple

class GraphNode:
    def __init__(self):
        self.color = 'w'
        self.distance = -1
        self.discover = -1
        self.finish = -1
        self.predecessor = None
        self.cc = -1
    def __lt__(self, another):
        return self.distance < another.distance

class Graph(Dict[GraphNode, List[GraphNode]]):
    def __init__(self):
        self.sorted: List[GraphNode] = []
        super().__init__()
