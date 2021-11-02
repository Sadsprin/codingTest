import sys
from collections import deque
input = sys.stdin.readline
q = deque()

def bfs2(ii, jj):
    global max_
    svisited = [[0] * column for i in range(row)]
    q.append((ii, jj))
    svisited[ii][jj] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in direction:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < row and 0 <= ny < column:
                if svisited[nx][ny]==0 and graph[nx][ny] == 'L':
                    svisited[nx][ny] = svisited[x][y] + 1
                    max_ = max(max_, svisited[nx][ny])
                    q.append((nx, ny))


row, column = map(int, input().split())
graph = [list(input().rstrip()) for i in range(row)]
visited = [[False] * column for i in range(row)]
max_ = 0
direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
for i in range(row):
    for j in range(column):
        if graph[i][j] == "L":
            bfs2(i, j)
print(max_-1)