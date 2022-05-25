def find_maximum_subarray(a):
    return _find_maximum_subarray(a, 0, len(a))

def _find_maximum_subarray(a, low, high):
    if low + 1 == high: return low, high, a[low]
    mid = (low + high) // 2
    llow, lhigh, lvalue = _find_maximum_subarray(a, low, mid)
    rlow, rhigh, rvalue = _find_maximum_subarray(a, mid, high)
    clow, chigh, cvalue = find_max_crossing_subarray(a, low, mid, high)
    value = max(lvalue, rvalue, cvalue)
    if value == lvalue: return llow, lhigh, lvalue
    elif value == rvalue: return rlow, rhigh, rvalue
    else: return clow, chigh, cvalue

def find_max_crossing_subarray(a, low, mid, high):
    left_sum = -2147483648
    left_idx = 0
    s = 0
    for idx in range(mid - 1, low - 1, -1):
        s += a[idx]
        left_sum = max(s, left_sum)
        left_idx = idx
    right_sum = -2147483648
    right_idx = 0
    s = 0
    for idx in range(mid, high):
        s += a[idx]
        right_sum = max(s, right_sum)
        right_idx = idx + 1
    return left_idx, right_idx, left_sum + right_sum

if __name__ == '__main__':
    print(find_maximum_subarray([3, -2, 2, 0, -3, -1, 2, 4, 1]))
