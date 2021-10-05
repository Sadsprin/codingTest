from heapq import heappush, heappop
import sys
input = sys.stdin.readline
q = []
res = []
for _ in range(int(input())):
    if (num := int(input())): heappush(q, num)
    else: print(heappop(q) if q else 0)
