from functools import reduce

def bisect_ricecake(array, start, end):
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for i in array:
            remain_cake = i - mid
            if remain_cake > 0:
                sum += remain_cake
        if sum >= M:
            possible = mid
            start = mid + 1
        else:
            end = mid - 1

    return possible

N, M = map(int, input().split())

height = list(map(int, input().split()))

print(bisect_ricecake(height, 0, max(height)))




    