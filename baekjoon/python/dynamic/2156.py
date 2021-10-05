import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dynamic(k):
    global dp
    if k < 3: return dp[k]
    if dp[k] != -1: return dp[k]
    dp[k] = max(dynamic(k-3) + L[k-1] + L[k], dynamic(k-1), dynamic(k-2) + L[k])
    return dp[k]

    

n = int(input())
L = [0] + [int(input()) for i in range(n)]
dp = [0] + [-1] * (n)
dp[1] = L[1]
if n != 1: dp[2] = L[1] + L[2]
print(dynamic(n))


