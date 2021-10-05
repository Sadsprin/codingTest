from heapq import heappush, heappop
import sys
input = sys.stdin.readline
q = []
res = []
for _ in range(int(input())):
    num = int(input())
    if num == 0:
        try: print(-heappop(q))
        except IndexError: print(0)
    else: heappush(q, -num)