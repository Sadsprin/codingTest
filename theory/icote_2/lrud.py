import time

import sys
input = sys.stdin.readline

N = int(input())
move = input().rstrip().split()
start = time.time()
vector = {
    'L' : (0, -1),
    'R' : (0, 1),
    'U' : (-1, 0),
    'D' : (1, 0),
}

x, y = 0, 0
twoDarray = [[0] * N for _ in range(N)]

for move_ in move:
    nx = x + vector[move_][0]
    ny = y + vector[move_][1]
    if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:
        continue
    x, y = nx, ny

print(x+1, y+1)
print("execute time : {}".format(time.time() - start))