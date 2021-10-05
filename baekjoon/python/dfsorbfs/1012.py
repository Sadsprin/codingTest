import sys
from pprint import pprint
read = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(x, y):
    global graph
    if x < 0 or x > n - 1 or y < 0 or y > m - 1:
        return False
    if graph[x][y] <= 0:
        return False
    graph[x][y] = -1
    for i in range(4):
        dfs(x + dx[i], y + dy[i])
    return True

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(int(read())):
    m, n, k = map(int, read().split())
    ans = 0
    graph = [[0] * m for _ in range(n)]
    for j in range(k):
        a, b = map(int, read().split())
        graph[b][a] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                if dfs(i, j):
                    ans += 1
    print(ans)