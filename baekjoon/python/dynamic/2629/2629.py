import sys
from pprint import pprint
input = sys.stdin.readline

n = int(input())
L = sorted(map(int, input().split()))
sum_L = sum(L)
dp = [[False] * (sum_L + 1) for _ in range(len(L)+1)]
for i in range(1, len(L)+1):
    for k in range(1, sum_L+1):
        if k < L[i-1] and dp[i-1][k]:
            dp[i][k] = True
            dp[i][L[i-1]-k] = True
        elif L[i-1] == k:
            dp[i][k] = True
        else:
            if dp[i-1][k]:
                dp[i][k] = True
                dp[i][k-L[i-1]]=True
            elif dp[i-1][k-L[i-1]]:
                dp[i][k] = True

int(input())
str_ = ''
for i in map(int, input().split()):
    if i > sum_L:
        str_ += 'N '
        continue
    if dp[len(L)][i]:
        str_ += 'Y '
    else:
        str_ += 'N '
print(str_)
    





