from graph.bellmanFord import relax
from graph.topologicalSort import topologicalSort
from .graph import Graph, GraphNode

def shortestPathDAG(graph: Graph, weight, source: GraphNode):
    for node in graph:
        node.predecessor = None
        node.distance = 2147483647
    source.distance = 0
    topologicalSort(graph)
    for node in graph.sorted:
        for neighbor in graph[node]:
            relax(node, neighbor, weight[(node, neighbor)])
