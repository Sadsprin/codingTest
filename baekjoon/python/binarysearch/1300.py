import sys
input = sys.stdin.readline

N = int(input())
index = int(input())

a, b = divmod(index - 1, N)

print((a + 1) * (b + 1))

