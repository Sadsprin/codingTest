import sys
input = sys.stdin.readline

def dfs(x, y):
    if x < 0 or y < 0 or x >= N or y >= N:
        return 0
    if graph[x][y] == 0:
        return 0
    graph[x][y] = 0
    return dfs(x, y - 1) + dfs(x - 1, y) + dfs(x, y + 1) + dfs(x + 1, y) + 1  



N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int, list(input().rstrip()))))

result = 0
apart_num = []
for i in range(N):
    for j in range(N):
        bool_ = dfs(i, j)
        if bool_ > 0:
            apart_num.append(bool_)
            result += 1
print(result)
apart_num.sort()
for i in apart_num:
    print(i)