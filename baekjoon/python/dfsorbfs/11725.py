import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
tree = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
visited = [False] * (n+1)
res = [0] * (n+1)
q = deque()
q.append((1, None))
while q:
    val, parent = q.popleft()
    visited[val] = True
    res[val] = parent
    for i in tree[val]:
        if not visited[i]:
            q.append((i, val))

print('\n'.join(map(str, res[2:])))