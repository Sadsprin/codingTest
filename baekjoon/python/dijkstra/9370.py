import sys
import heapq
input = sys.stdin.readline

T = int(input())
INF = int(1e9)
def dijkstra(start, end, n, graph):
    distance = [INF] * (n+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        cost, index = heapq.heappop(q)
        if index == end:
            return cost
        if distance[index] < cost:
            continue
        for i in graph[index]:
            cost = distance[index] + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return INF



for i in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())
    graph = [[] for i in range(n+1)]
    for _ in range(m):
        a,b,c = map(int, input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    tl = []
    for _ in range(t):
        tl.append(int(input()))
    res = []
    for i in tl:
        s_g = dijkstra(s,g,n,graph)
        g_h_g = dijkstra(g,h,n,graph)
        h_i = dijkstra(h,i,n,graph)
        s_h = dijkstra(s,h,n,graph)
        g_i = dijkstra(g,i,n,graph)
        ans = min(s_g + g_h_g + h_i, s_h + g_h_g + g_i)
        s_i = dijkstra(s,i,n,graph)
        if ans == s_i:
            res.append(i)
    print(*sorted(res))
    
        


