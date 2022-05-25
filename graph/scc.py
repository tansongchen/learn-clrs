from .graph import Graph, GraphNode

def scc(graph: Graph):
    for node in graph:
        if node.color == 'w':
            dfsVisitSort(node, graph)
    transposed: Graph = {}
    for node in graph:
        transposed[node] = []
    for node, adjList in graph.items():
        for neighbor in adjList:
            transposed[neighbor].append(node)
    graph.sorted.reverse()
    for node in graph.sorted:
        node.color = 'w'
    cc = 0
    for node in graph.sorted:
        if node.color == 'w':
            node.cc = cc
            dfsVisit(node, graph)
            cc += 1
    component = Graph()
    for i in range(cc):
        component[i] = set()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            if neighbor.cc != node.cc:
                component[node.cc].add(neighbor.cc)
    for i in range(cc):
        component[i] = list(component[i])

def dfsVisitSort(node: GraphNode, graph: Graph):
    node.color = 'g'
    for neighbor in graph[node]:
        if neighbor.color == 'w':
            neighbor.cc = node.cc
            dfsVisitSort(neighbor, graph)
    graph.sorted.append(node)

def dfsVisit(node: GraphNode, graph: Graph):
    node.color = 'g'
    for neighbor in graph[node]:
        if neighbor.color == 'w':
            neighbor.cc = node.cc
            dfsVisit(neighbor, graph)
