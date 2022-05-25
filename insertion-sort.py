def insertion_sort(a: list):
    for i in range(1, len(a)):
        key = a[i]
        j = i
        while j > 0 and a[j - 1] > key:
            a[j] = a[j - 1]
            j -= 1
        a[j] = key

def insertion_sort_reverse(a: list):
    for i in range(1, len(a)):
        key = a[i]
        j = i
        while j > 0 and a[j - 1] < key:
            a[j] = a[j - 1]
            j -= 1
        a[j] = key

if __name__ == '__main__':
    a = [28, 35, 14, 3]
    insertion_sort(a)
    print(a)
