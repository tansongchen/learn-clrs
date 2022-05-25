def longestMonotonicalSubsequence(a):
    n = len(a)
    l = [1 for _ in range(n)]
    for i in range(1, n):
        for j in range(i):
            if a[i] > a[j]:
                l[i] = max(l[i], l[j] + 1)
    return l[-1]
