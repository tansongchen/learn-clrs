from random import randrange

def randomized_partition(a, p, r):
    i = randrange(p, r)
    a[i], a[r - 1] = a[r - 1], a[i]
    return partition(a, p, r)

def partition(a, p, r):
    pivot = a[r - 1]
    i = p
    for j in range(p, r - 1):
        if a[j] <= pivot:
            a[i], a[j] = a[j], a[i]
            i += 1
    a[i], a[r - 1] = a[r - 1], a[i]
    return i

def randomized_select(a, i):
    return _randomized_select(a, 0, len(a), i)

def _randomized_select(a, p, r, i):
    if p + 1 == r: return a[p]
    q = randomized_partition(a, p, r)
    k = q - p + 1
    if k == i: return a[q]
    elif k > i: return _randomized_select(a, p, q, i)
    else: return _randomized_select(a, q + 1, r, i - k)

def randomized_select_iterative(a, i):
    p, r = 0, len(a)
    while p + 1 < r:
        q = randomized_partition(a, p, r)
        k = q - p + 1
        if k == i: return a[q]
        elif k > i: r = q
        else: p, i = q + 1, i - k
    return a[p]

if __name__ == '__main__':
    print(randomized_select([3, 2, 6, 7, 1, 5], 3))
    print(randomized_select_iterative([3, 2, 6, 7, 1, 5], 3))
