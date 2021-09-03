import sys
from collections import deque
import copy
from pprint import pprint
input = sys.stdin.readline


def bfs_island(x, y):
    global island_num
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    graph[x][y] = island_num

    while q:
        xx, yy = q.popleft()
        for k in range(4):
            nx = xx + dx[k]
            ny = yy + dy[k]
            if 0 <= nx < N and 0 <= ny < N and graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                graph[nx][ny] = island_num
                q.append([nx, ny])



def bfs(region):
    global min
    for i in range(N):
        for j in range(N):
            if graph[i][j] == region:
                queue.append((i, j))
    dist = copy.deepcopy(graph)
    while queue:
        xx, yy = queue.popleft()
        for i in range(4):
            nx = xx + dx[i]
            ny = yy + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >=N:
                continue
            if dist[nx][ny] == 0:
                queue.append((nx, ny))
                if dist[xx][yy] < 0:
                    dist[nx][ny] += 1
                else:
                    dist[nx][ny] = dist[xx][yy] + 1
                #pprint(dist)

            if dist[nx][ny] != region and dist[nx][ny] < 0:
                if min >= dist[xx][yy]:
                    min = dist[xx][yy]
    return True

min = 10001
N = int(input())
visited = [[False] * N for _ in range(N)]
graph = []
region_n = []
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
for _ in range(N):
    graph.append(list(map(int, input().split())))
island_num = -1

for i in range(N):
    for j in range(N):
        if not visited[i][j] and graph[i][j] == 1:
            region_n.append(island_num)
            bfs_island(i, j)
            island_num -= 1
queue = deque()
for i in region_n:
    bfs(i)
            
print(min)