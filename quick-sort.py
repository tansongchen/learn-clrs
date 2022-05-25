from random import randrange

def randomized_quick_sort(a):
    _randomized_quick_sort(a, 0, len(a))

def quick_sort(a):
    _quick_sort(a, 0, len(a))

def _quick_sort(a, p, r):
    if p + 1 < r:
        q = partition(a, p, r)
        _quick_sort(a, p, q)
        _quick_sort(a, q + 1, r)

def _randomized_quick_sort(a, p, r):
    if p + 1 < r:
        q = randomized_partition(a, p, r)
        _quick_sort(a, p, q)
        _quick_sort(a, q + 1, r)

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

if __name__ == '__main__':
    a = [1, 5, 3, 6]
    quick_sort(a)
    print(a)
    b = [4, 3, 8, 2, 1, 9]
    randomized_quick_sort(b)
    print(b)
