import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def recur(start):
    global parent
    if dp[start] != -1: return dp[start]
    tmp = 0
    parent |= {start}
    for i in graph[start]:
        if i not in parent:
            tmp += recur(i)
    if tmp == 0:
        dp[start] = 1
        return dp[start]
    dp[start] = tmp + 1
    return dp[start]

parent = set()
N, R, Q = map(int, input().split())
dp = [-1] * (N+1)
tree = [[] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
recur(R)
for i in range(Q):
    print(dp[int(input())])

