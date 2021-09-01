import sys
from collections import deque
input = sys.stdin.readline

def dfs(start, graph_sort, isvisited):
    isvisited[start] = True
    print(str(start) + ' ' ,end='')
    for i in graph_sort[start]:
        if not isvisited[i]:
            dfs(i, graph_sort, isvisited)

def bfs(start, graph_sort, isvisited):
    queue = deque([start])
    isvisited[start] = True
    while queue:
        popv = queue.popleft()
        print(str(popv) + ' ', end='')
        for i in graph_sort[popv]:
            if not isvisited[i]:
                isvisited[i] = True
                queue.append(i)


n, m, start = map(int, input().split())

graph = [[] for _ in range(n + 1)]
isvisited = [False] * (n + 1)
for _ in range(m):
    f, s = map(int, input().split())
    graph[f].append(s)
    graph[s].append(f)

graph_sort = list(map(lambda x: sorted(x), graph))

dfs(start, graph_sort, isvisited)
isvisited = [False] * (n + 1)
print("")
bfs(start, graph_sort, isvisited)
