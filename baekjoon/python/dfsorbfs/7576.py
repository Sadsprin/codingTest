import sys
from collections import deque
read = sys.stdin.readline
def fourdirec(xpos, ypos):
    return [(xpos + 1, ypos), (xpos, ypos + 1), (xpos - 1, ypos), (xpos, ypos - 1)]

def bfs(queue):
    global graph, n, m
    while queue:
        xx, yy = queue.popleft()
        for i in fourdirec(xx, yy):
            nx, ny = i
            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0 and graph[nx][ny] != -1 :
                graph[nx][ny] = graph[xx][yy] + 1
                queue.append((nx, ny))




n, m = map(int, read().split())
graph = []
for i in range(m):
    graph.append([int(i) for i in read().split()])
queue = deque()
for i in range(m):
    for j in range(n):
        if graph[i][j] == 1:
            queue.append((i, j))
bfs(queue)
reap = False
for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            reap = True

if reap:
    print(-1)
else:
    max_ = 0
    for i in range(m):
        max_ = max(max_, max(graph[i]))
    print(max_ - 1)



