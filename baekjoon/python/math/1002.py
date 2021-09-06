import sys
input = sys.stdin.readline

T = int(input())
for i in range(3):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = ((x2 - x1) **2 + (y2 - y1) **2)**0.5
    if dis == r1 **2 + r2 **2:
        print(-1)
    elif dis > r1 + r2:
        print(0)
    elif dis < r1 + r2:
        print(2)
    else:
        print(1)