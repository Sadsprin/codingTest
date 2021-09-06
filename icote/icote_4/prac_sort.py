import time
from random import randint
from sortAlgorithm import quick
import sys
sys.setrecursionlimit(10**9)
N, K = map(int, input().split())

f = [1,2,3,4,5,6,7,8,9]
s = [5,4,3,2]

start = time.time()
quick(f)
quick(s, reverse=True)

for i in range(K):
    if f[i] < s[i]:
        f[i], s[i] = s[i], f[i]

print(sum(f))
print("execute time :", time.time() - start )