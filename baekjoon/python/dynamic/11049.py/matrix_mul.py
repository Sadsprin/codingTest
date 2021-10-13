import sys
from pprint import pprint
input = sys.stdin.readline
n = int(input())
L = [tuple(map(int, input().split())) for i in range(n)]
dp = [[0 for i in range(n)] for i in range(n)]
for i in range(n):
    dp[i][i] = (0, (L[i][0], L[i][1]))
INF = int(1e9)
for j in range(1, n):
    for i in range(j-1,-1,-1):
        small = INF
        for k in range(j-i):
            s = dp[i][i+k][0]
            e = dp[i+k+1][j][0]
            f_s, f_e = dp[i][i+k][1]
            s_s, s_e = dp[i+k+1][j][1]
            tmp = s + e + f_s * s_s * s_e
            if small > tmp:
                small = tmp
                ma = (f_s, s_e)
        dp[i][j] = (small, ma)
pprint(dp[0][n-1][0])



