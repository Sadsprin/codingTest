from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        print("x : {}   y : {}".format(x, y))
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny>= m:
                continue
            elif graph[nx][ny] == 0:
                continue
            elif graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                break
    return graph[n - 1][m - 1]


n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, list(input()))))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

print(bfs(0, 0))