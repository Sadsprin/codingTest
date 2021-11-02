import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    global visited, graph
    q = deque([start])
    istree = True
    while q:
        curr = q.popleft()
        if visited[curr]:
            istree = False
        visited[curr] = True
        for i in graph[curr]:
            if not visited[i]:
                q.append(i)
    return istree
num = 0
while (num:=num+1):
    vn, en = map(int, input().split())
    if vn == 0 and en == 0: break
    graph = [[] for i in range(vn+1)]
    visited = [False] * (vn+1)
    for i in range(en):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    res = 0
    for i in range(1, vn+1):
        if not visited[i]:
            if bfs(i):
                res += 1
    if res == 0:
        print(f'Case {num}: No trees.')
    elif res == 1:
        print(f'Case {num}: There is one tree.')
    else:
        print(f'Case {num}: A forest of {res} trees.')
