import sys
from pprint import pprint
input = sys.stdin.readline

def check(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1
    if dp[x][y] != -1:
        return dp[x][y]
    dp[x][y] = 0
    for dx, dy in [(0,1), (1, 0), (0, -1), (-1, 0)]:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] < graph[x][y]:
                dp[x][y] += dfs(nx, ny)
    return dp[x][y]

n, m = map(int, input().split())
graph = []
dp = [[-1 for i in range(m)] for i in range(n)]
visited = [[False for i in range(m)] for i in range(n)]
for i in range(n):
    graph.append([*map(int, input().split())])
print(dfs(0, 0))
