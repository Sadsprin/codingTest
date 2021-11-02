import sys
input = sys.stdin.readline

T = int(input())
for i in range(3):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    if x1 == y1 and y1 == y2:
        if r1 == r2: print(-1)
        else: print(0)
        break

    dis = ((x2 - x1) **2 + (y2 - y1) **2)**0.5

