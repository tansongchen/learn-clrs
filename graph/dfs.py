from graphAL import Graph, GraphNode

def dfs(graph: Graph):
    graph.time = 0
    for node in graph:
        if node.color == 'w':
            dfsVisit(node, graph)

def dfsVisitIterative(node: GraphNode, graph: Graph):
    stack = [node]
    while stack:
        node = stack.pop()
        if node.color == 'g':
            node.color = 'b'
            node.finish = graph.time
            graph.time += 1
            continue
        node.color = 'g'
        node.discover = graph.time
        graph.time += 1
        stack.append(node)
        for neighbor in graph[node]:
            if neighbor.color == 'w':
                neighbor.predecessor = node
                stack.append(neighbor)

def dfsVisit(node: GraphNode, graph: Graph):
    node.color = 'g'
    node.discover = graph.time
    graph.time += 1
    for neighbor in graph[node]:
        if neighbor.color == 'w':
            neighbor.predecessor = node
            dfsVisit(neighbor, graph)
    node.color = 'b'
    node.finish = graph.time
    graph.time += 1
