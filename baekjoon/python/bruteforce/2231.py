import sys

N = int(sys.stdin.readline())
first = N - 54 if N > 54 else 0

for i in range(first, N):
    M = i + sum(map(int, list(str(i))))
    if M == N:
        print(i)
        break
    if i == N - 1:
        print(0)