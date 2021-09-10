import sys
from itertools import combinations
a, b = map(int, sys.stdin.readline().split())

range_list = list(range(1, a+1))

res = list(combinations(range_list, b))

for i in res:
    print(' '.join(list(map(str, i))))



