import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

def counting(array, target):
    return bisect_right(array, target) - bisect_left(array, target)

N, x = map(int, input().split())
num = list(map(int, input().split()))

result = counting(num, x)

print(result if result != 0 else -1)
