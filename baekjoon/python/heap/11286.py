import heapq
import sys
input = sys.stdin.readline
L = [int(input()) for i in range(int(input()))]
q = []
a = lambda x, y: x * y
for i in L:
    if i != 0:
        heapq.heappush(q, (abs(i), int(i / abs(i))))
    else:
        if q:
            print(a(*heapq.heappop(q)))
        else:
            print(0)