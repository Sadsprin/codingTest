import sys
input = sys.stdin.readline
INF = int(1e9)
n, m = map(int, input().split())
visited = [False] * (n+1)
graph = [[INF] * (n+1) for i in range(n+1)]
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
temp = INF
for i in range(1, n+1):
    for j in range(i, n+1):
        if i!=j: temp = min(temp, graph[i][j] + graph[j][i])

if temp == INF: print(-1)
else: print(temp)


