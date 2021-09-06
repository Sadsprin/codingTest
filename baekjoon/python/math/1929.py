import sys

input = sys.stdin.readline
M, N = map(int, input().split())

num = [True] * (N + 1)
m = int(N ** 0.5)
num[1] = False
for i in range(2, m + 1):
    if num[i] == True:
        for j in range(i * i, N+1, i):
            num[j] = False
for i in range(M, N+1):
    if num[i] == True:
        print(i)


