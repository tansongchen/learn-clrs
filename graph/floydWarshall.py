from graph.graph import Graph


def floydWarshall(graph: Graph, weight):
    n = len(graph)
    D = [[0 for _ in range(n)] for _ in range(n)]
    Dnew = [[0 for _ in range(n)] for _ in range(n)]
    nodes = list(graph.keys())
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            edge = (nodes[i], nodes[j])
            D[i][j] = weight.get(edge, 2147483647)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                Dnew[i][j] = min(D[i][j], D[i][k] + D[k][j])
        D = Dnew
    return D
