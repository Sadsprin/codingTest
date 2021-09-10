import sys
from itertools import product
a, b = map(int, sys.stdin.readline().split())

range_list = list(range(1, a+1))

res = list(product(range_list, repeat=b))

for i in res:
    print(' '.join(list(map(str, i))))