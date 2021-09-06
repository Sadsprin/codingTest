import sys
input = sys.stdin.readline

N = int(input())
currPrize = 0
failCount = 0
for i in range(N):
    x, p = map(int, input().split())
    if x >= currPrize: currPrize += p; print(i, "yes", currPrize)
    else:
        failCount += 1; print(i, "No")
        if failCount == 2: print("Zzz"); break
    if x == N-1: print("Kkeo-eok")

    

