import sys
from pprint import pprint
input = sys.stdin.readline

def dfs(graph, isvisited, start, virus):
    isvisited[start] = True
    virus += 1
    for i in graph[start]:
        if not isvisited[i]:
            virus = dfs(graph, isvisited, i, virus)
    return virus






comN = int(input())
isvisited = [False] * (comN + 1)
graph = [[] for i in range(comN + 1)]
virus = 0
for i in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(dfs(graph, isvisited, 1, virus) - 1)


