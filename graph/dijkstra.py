from graph.graph import Graph, GraphNode
from heapq import heappush, heappop

def dijkstra(graph: Graph, source: GraphNode):
    for node in graph:
        node.predecessor = None
        node.distance = 2147483647
    source.distance = 0
    queue = [source]
    seen = set()
    while queue:
        node = heappop(queue)
        if node in seen:
            continue
        seen.add(node)
        for neighbor in graph[node]:
            if neighbor.distance > node.distance + weight[(node, neighbor)]:
                neighbor.distance = node.distance + weight[(node, neighbor)]
                neighbor.predecessor = node
            heappush(neighbor)
