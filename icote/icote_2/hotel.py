import sys

N = int(sys.stdin.readline())

for _ in range(N):
    h, w, n = list(map(int, sys.stdin.readline().strip().split()))
    ho, floor = divmod(n, h)
    b = ho if floor == 0 else ho + 1  
    print(str(floor if floor != 0 else str(h)) + ('0' + str(b) if b < 10 else str(b)))