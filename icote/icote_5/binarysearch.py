def binarySearch_recur(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarySearch_recur(array, target, start, mid - 1)
    else:
        return binarySearch_recur(array, target, mid + 1, end)

def binarySearch_loop(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

array = list(range(1,19,2))
print(array)

print(binarySearch_loop(array, 17, 0, 8))