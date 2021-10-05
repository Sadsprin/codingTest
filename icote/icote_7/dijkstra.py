import sys
input = sys.stdin.readline
INF = 10e9
vertex_n, edge_n = map(int, input().split())

start = int(input())

graph = [[] for i in range(vertex_n + 1)]
for i in range(edge_n):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))

distance = [INF] * (vertex_n + 1)
visited = [False] * (vertex_n + 1)
print(graph)
def shortest_node():
    min_value = INF
    index = 0
    for i in range(1, vertex_n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index


def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for i in graph[start]:
        distance[i[0]] = i[1]
    for j in range(vertex_n - 1):
        print(distance)
        now = shortest_node()
        print(now)
        visited[now] = True
        for k in graph[now]:
            if distance[now] + k[1] < distance[k[0]]:
                distance[k[0]] = distance[now] + k[1]
    return distance

print(dijkstra(1))


