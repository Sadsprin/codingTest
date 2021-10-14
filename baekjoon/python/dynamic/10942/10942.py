import sys
input = sys.stdin.readline
n = int(input())
L = [*map(int, input().split())]
dp = [[-1 if i != j else 1 for j in range(n)] for i in range(n)]

for j in range(1, n):
    for i in range(j-1, -1, -1):
            if L[i] == L[j]:
                if i + 2 < j and not dp[i+1][j-1]:
                    dp[i][j] = 0
                    continue
                dp[i][j] = 1
            else:
                dp[i][j] = 0

res = ''
for i in range(int(input())):
    x, y = map(int, input().split())
    res += '1\n' if dp[x-1][y-1] else '0\n'
print(res)

