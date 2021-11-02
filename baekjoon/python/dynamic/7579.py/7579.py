import sys
input = sys.stdin.readline
n, m = map(int, input().split())
L1 = map(int, input().split())
L2 = [*map(int, input().split())]
L = [*zip(L1, L2)]
dp = [[0] * (sum(L2)+1) for i in range(n+1)]
for idx , val in enumerate(L, start = 1):
    byte, t = val
    for i in range(sum(L2)+1):
        if i < t:
            dp[idx][i] = dp[idx - 1][i]
        else:
            dp[idx][i] = max(dp[idx - 1][i], dp[idx - 1][i - t] + byte)
for idx, i in enumerate(zip(*dp)):
    if max(i) >= m:
        print(idx)
        break