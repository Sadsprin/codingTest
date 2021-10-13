import sys
from pprint import pprint
arr = []
for i in range(9):
    arr.append([int(i) for i in sys.stdin.readline().split()])
arr1 = list(map(set, zip(*arr)))
arr2 = [[] for i in range(9)]
for idx, kk in enumerate(arr):
    for k in range(3):
        arr2[(idx//3)*3 + k].extend(kk[k*3: k*3 + 3])
pprint(arr2)

empty_list = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            empty_list.append((i, j))

print(empty_list)
print(arr1)
