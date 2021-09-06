import sys

A, B, V = map(int, sys.stdin.readline().split())
Vab = V - A - 1
ans = Vab // (A-B) + 2
print(ans)




