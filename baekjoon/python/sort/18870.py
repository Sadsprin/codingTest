import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))
num_set = sorted(set(num))

for i in num:
    print(bisect_left(num_set, i), end=" ")






