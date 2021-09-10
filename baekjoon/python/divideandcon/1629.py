import sys
input = sys.stdin.readline

def powerofnum(a, b, c):
    if b == 0: return 1
    elif b % 2 == 0: n = powerofnum(a, b//2, c); return n * n % c
    else: n = powerofnum(a, (b-1)//2, c); return a * n * n % c

a, b, c = map(int, input().split())
print(powerofnum(a, b, c))