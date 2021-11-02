import sys
from pprint import pprint
arr = []
for i in range(9):
    arr.append([int(i) for i in sys.stdin.readline().split()])
 
empty_list = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]

