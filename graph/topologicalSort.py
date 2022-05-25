from .graph import Graph, GraphNode

def topologicalSort(graph: Graph):
    for node in graph:
        if node.color == 'w':
            dfsVisit(node, graph)
    graph.sorted.reverse()

def dfsVisit(node: GraphNode, graph: Graph):
    node.color = 'g'
    for neighbor in graph[node]:
        if neighbor.color == 'w':
            dfsVisit(neighbor)
    graph.sorted.append[node]
