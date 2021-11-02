import sys
from collections import deque
read = sys.stdin.readline


def bfs(graph, start, end):
    global m
    global n
    queue = deque([(start, end)])
    while queue:
        xx, yy = queue.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[xx][yy] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]

n, m = map(int, read().split())
graph = []
for _ in range(n):
    graph.append([int(i) for i in list(read().rstrip())])
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
print(bfs(graph, 0, 0))
