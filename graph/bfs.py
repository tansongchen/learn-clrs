from graphAL import Graph, GraphNode
from collections import deque as Queue

def bfs(graph: Graph):
    for node in graph:
        if node.color == 'w':
            bfsVisit(node)

def bfsVisit(node: GraphNode, graph: Graph):
    node.color = 'g'
    node.distance = 0
    queue = Queue([node])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor.color == 'w':
                neighbor.color == 'g'
                neighbor.predecessor = node
                neighbor.distance = node.distance + 1
                queue.append(neighbor)
        node.color = 'b'
