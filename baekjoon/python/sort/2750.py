import sys
input = sys.stdin.readline
N = int(input())
num = []
for i in range(N):
    num.append(int(input()))
for i in sorted(num):
    print(i)

# def quick(array):
#     if len(array) <= 1:
#         return array
#     pivot = array[0]
#     left = array[1:]
#     left_side = [x for x in left if x <= pivot]
#     right_side = [x for x in left if x > pivot]

#     return quick(left_side) + [pivot] + quick(right_side)

# def select(array):
#     for i in range(len(array) - 1):
#         for j in range(i+1, len(array)):
#             if array[i] > array[j]:
#                 array[i], array[j] = array[j], array[i]
#     return array
# sort_num = select(num)
# for i in sort_num:
#     print(i)