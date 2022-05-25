def merge_sort(a: list):
    return merge_sort_rec(a, 0, len(a))

def merge_sort_rec(a: list, start: int, end: int):
    if start + 1 < end:
        middle = (start + end) // 2
        merge_sort_rec(a, start, middle)
        merge_sort_rec(a, middle, end)
        merge_without_setinels(a, start, middle, end)

def merge(a: list, start: int, middle: int, end: int):
    l = a[start : middle]
    r = a[middle : end]
    l.append(2147483647)
    r.append(2147483647)
    inl = inr = 0
    for i in range(start, end):
        if l[inl] <= r[inr]:
            a[i] = l[inl]
            inl += 1
        else:
            a[i] = r[inr]
            inr += 1

def merge_without_setinels(a: list, start: int, middle: int, end: int):
    l = a[start : middle]
    r = a[middle : end]
    inl = inr = 0
    for i in range(start, end):
        if inl == len(l):
            a[i] = r[inr]
            inr += 1
        elif inr == len(r):
            a[i] = l[inl]
            inl += 1
        elif l[inl] <= r[inr]:
            a[i] = l[inl]
            inl += 1
        else:
            a[i] = r[inr]
            inr += 1

if __name__ == '__main__':
    a = [28, 35, 14, 3]
    merge_sort(a)
    print(a)
