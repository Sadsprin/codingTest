import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
vertex, edge = map(int, input().split())
start = int(input())
graph = [[] for i in range(vertex + 1)]
for i in range(edge):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (vertex + 1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        cost, vert = heapq.heappop(q)
        if distance[vert] < cost:
            continue
        for i in graph[vert]:
            cost = distance[vert] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))

dijkstra(start)

for i in range(1, vertex+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

