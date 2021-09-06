import time

# select sorting
# for i in range(len(n)):
#     min_index = i
#     for j in range(i+1, len(n) - 1):
#         if n[i] > n[j]:
#             min_index = j
#     n[i], n[min_index] = n[min_index], n[i]

# insert sorting
# for i in range(1, len(n)):
#     for j in range(i, 0, -1):
#         if n[j] < n[j-1]:
#             n[j], n[j - 1] = n[j-1], n[j]
#         else:
#             break
# #n = [1,4,2,0,3]

# quick sort v.1
# def quick(n, start, end):
#     if start >= end:
#         return
#     pivot = start
#     left = start + 1
#     right = end
#     while left <= right:
#         while left <= end and n[left] <= n[pivot]:
#             left += 1
#         while right > start and n[right] >= n[pivot]:
#             right -= 1
#         if left > right:
#             n[pivot], n[right] = n[right], n[pivot]
#         else:
#             n[left], n[right] = n[right], n[left]
    
#     quick(n, start, right -1)
#     quick(n, right + 1, end)

# quick(nn, 0, len(nn) - 1 )

# quick sort v.2
# nn = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def quick(array, reverse=False):
    if len(array) <=1:
        return array
    pivot = array[0]
    tail = array[1:]
    if not reverse:
        left_side = [x for x in tail if x <= pivot]
        right_side = [x for x in tail if x > pivot]
    else:
        left_side = [x for x in tail if x > pivot ]
        right_side = [x for x in tail if x <= pivot]
    return quick(left_side, reverse) + [pivot] + quick(right_side, reverse)

# print(quick(nn,reverse= True))
