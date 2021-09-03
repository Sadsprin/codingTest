import sys
input = sys.stdin.readline
from functools import reduce

T = int(input())
for _ in range(T):
    a, *b = map(int, input().rstrip().split())
    avg = sum(b) / a
    a = str(round(reduce(lambda acc, cur: acc + 1 if cur > avg else acc, b, 0) / a * 100, 3))
    c = a.ljust(5,'0') if float(a) < 10 else a.ljust(6, '0')
    print(c+'%')
