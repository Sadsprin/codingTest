import sys
input = sys.stdin.readline
M = int(input())
N = int(input())

sieve = [True] * N

m = int(N ** 0.5)

for i in range(2, m+1):
    if sieve[i] == True:
        for j in range(2 * i, N, i):
            sieve[j] = False









