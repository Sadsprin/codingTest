import sys
# from bisect import bisect_left, bisect_right
input = sys.stdin.readline
from collections import Counter
N = int(input())
arr = list(map(int, input().split()))
count = Counter(arr)
# arr.sort()
M = int(input())
for i in map(int, input().split()):
     print(count[i], end=" ")





