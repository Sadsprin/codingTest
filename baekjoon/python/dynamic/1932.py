import sys
input = sys.stdin.readline

def sol(N):
    for i in range(1, N):
        for j in range(i + 1):
            if j == 0: dp[i][j] = tri[i][j] + dp[i - 1][j]
            elif j == i: dp[i][j] = tri[i][j] + dp[i - 1][j - 1]
            else: dp[i][j] = max(tri[i][j] + dp[i - 1][j], tri[i][j] + dp[i - 1][j - 1])
    return max(dp[N-1])



N = int(input())
tri = []
for i in range(N):
    tri.append(list(map(int, input().split())))
dp = [[0] * N for i in range(N)]
dp[0][0] = tri[0][0]
print(sol(N))