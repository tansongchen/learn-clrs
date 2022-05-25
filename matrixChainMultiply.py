def matrixChainMultiply(A, s, i, j):
    if i + 1 == j:
        return A[i]
    k = s[i][j]
    return matrixChainMultiply(A, s, i, k) * matrixChainMultiply(A, s, k, j)
