import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
for i in map(int, input().split()):
    ans = bisect_right(arr, i) - bisect_left(arr, i)
    print(ans, end=" ")




