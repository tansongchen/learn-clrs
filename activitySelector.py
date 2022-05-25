# the DP solution
def activitySelectorDP(s, f):
    n = len(s)
    s.insert(0, -1)
    s.append(2147483647)
    f.insert(0, 0)
    f.append(2147483647)
    c = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(n + 2):
        c[i][i] = 0
    for i in range(n + 1):
        c[i][i + 1] = 0
    for l in range(2, n + 2):
        for i in range(n + 2 - l):
            for j in range(i + 1, i + l):
                if s[j] > f[i] and f[j] < s[i + l]:
                    c[i][i + l] = max(c[i][i + l], 1 + c[i][j] + c[j][i + l])
    return c[0][n + 1]
