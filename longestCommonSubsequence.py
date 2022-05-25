def longestCommonSubsequence(x, y):
    n = len(x)
    m = len(y)
    c = [[0 for i in range(n + 1)] for j in range(m + 1)]
    b = [['' for i in range(n)] for j in range(m)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[j] == y[i]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 'ul'
            elif c[i - 1][j] >= c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 'u'
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 'l'
    s = ''
    ridx, cidx = m, n
    while ridx or cidx:
        if b[ridx][cidx] == 'ul':
            s = x[cidx - 1] + s
        elif b[ridx][cidx] == 'u':
            ridx -= 1
        else:
            cidx -= 1
    return (c[m][n], s)
