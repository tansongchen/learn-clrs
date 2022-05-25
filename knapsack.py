def zeroOneKnapsack(w, v, wmax):
    n = len(w)
    c = [[0 for _ in range(wmax + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1, 1):
        for l in range(1, wmax + 1, 1):
            c[i][l] = c[i - 1][l]
            if w[i] <= l:
                c[i][l] = max(c[i][l], v[i] + c[i][l - w[i]])
    return c[-1][-1]

def zeroOneKnapsackOptimized(w, v, wmax):
    n = len(w)
    c = [0 for _ in range(wmax + 1)]
    for i in range(1, n + 1, 1):
        for l in range(wmax, 0, -1):
            if w[i] <= l:
                c[l] = max(c[l], v[i] + c[l - w[i]])
    return c[-1]
