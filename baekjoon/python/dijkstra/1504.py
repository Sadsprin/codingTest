import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
vertex, edge = map(int, input().split())
graph = [[] for i in range(vertex + 1)]
for i in range(edge):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

distance = [INF] * (vertex + 1)

def dijkstra(start, end):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        cost, vert = heapq.heappop(q)
        if vert == end:
            return cost
        if distance[vert] < cost:
            continue
        for i in graph[vert]:
            cost = distance[vert] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost, i[0]))
    return INF
ans1=0
ans2=0
for i in [(1, v1), (v1, v2), (v2, vertex)]:
    ans1 += dijkstra(*i)
    distance = [INF] * (vertex + 1)

for i in [(1, v2), (v2, v1), (v1, vertex)]:
    ans2 += dijkstra(*i)
    distance = [INF] * (vertex + 1)
ans = min(ans1, ans2)

if ans >= INF: print(-1)
else: print(ans)
