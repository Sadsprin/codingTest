import sys
A, B, C = map(int, sys.stdin.readline().split())
print(A // (C - B) + 1 if B < C else -1)