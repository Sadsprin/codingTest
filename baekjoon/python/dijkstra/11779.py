import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
dist = [INF] * (n:=int(input())+1)
graph = [{} for i in range(n)]
visited = [False] * n

for i in range(int(input())):
    a, b, c = map(int, input().split())
    if b in graph[a]:
        if graph[a][b] > c:
            graph[a][b] = c
    else:
        graph[a][b] = c

start, end = map(int, input().split())

q = []
heapq.heappush(q, (0, start))
dist[start] = 0
while q:
    cost, curr = heapq.heappop(q)
    if dist[curr] < cost:
        continue
    if curr == end:
        print(cost)
    visited[curr] = True
    for i in graph[curr].items():
        cost = dist[curr] + i[1]
        if dist[i[0]] > cost and not visited[i[0]]:
            dist[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
    

    
