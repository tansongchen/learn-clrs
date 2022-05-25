def build_max_heap(a):
    heapsize = len(a) - 1
    for i in range(heapsize // 2, 0, -1):
        max_heapify(a, heapsize, i)

def max_heapify(a, heapsize, i):
    l = 2 * i
    r = 2 * i + 1
    largest = i
    if l <= heapsize and a[l] > a[largest]: largest = l
    if r <= heapsize and a[r] > a[largest]: largest = r
    if largest != i:
        a[largest], a[i] = a[i], a[largest]
        max_heapify(a, heapsize, largest)

def heapsort(a):
    build_max_heap(a)
    for heapsize in range(len(a) - 1, 1, -1):
        a[1], a[heapsize] = a[heapsize], a[1]
        max_heapify(a, heapsize - 1, 1)

if __name__ == '__main__':
    a = [0, 3, 7, 5, 8, 2, 1, 4, 6]
    heapsort(a)
    print(a)
