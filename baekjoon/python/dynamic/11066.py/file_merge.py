import sys
INF = 1000000001
input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    L = [*map(int, input().split())]
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(1,n):
        for i in range(j-1, -1, -1):
                min_ = INF
                for k in range(j-i):
                    min_ = min(min_, dp[i][i+k] + dp[i+k+1][j])
                dp[i][j] = min_ + sum(L[i:j+1])
    print(dp[0][n-1])
