from .graph import Graph, GraphNode

def relax(node: GraphNode, neighbor: GraphNode, weight: int):
    if neighbor.distance > node.distance + weight:
        neighbor.distance = node.distance + weight
        neighbor.predecessor = node

def bellmanFord(graph: Graph, weight, source: GraphNode):
    for node in graph:
        node.predecessor = None
        node.distance = 2147483647
    source.distance = 0
    for i in range(len(graph)):
        for node, neighborList in graph.items():
            for neighbor in neighborList:
                relax(node, neighbor, weight[(node, neighbor)])
