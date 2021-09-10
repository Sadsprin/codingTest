import sys
input = sys.stdin.readline
def sol(n):
    for i in range(1, n):
        for j in range(3):
            if j == 0: dp[i][j] = min(res[i][j] + dp[i - 1][j + 1], res[i][j] + dp[i - 1][j + 2] )
            elif j == 1: dp[i][j] = min(res[i][j] + dp[i - 1][j - 1], res[i][j] + dp[i - 1][j + 1] )
            else: dp[i][j] = min(res[i][j] + dp[i - 1][j - 2], res[i][j] + dp[i - 1][j - 1] )
    return min(dp[n - 1][0], dp[n - 1][1], dp[n  - 1][2])
    
res = []
N = int(input())
for _ in range(N):
    res.append(list(map(int, input().split())))
dp = [[0, 0, 0] for i in range(N)]
for i in range(3): dp[0][i] = res[0][i]
print(sol(N))


