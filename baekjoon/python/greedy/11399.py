from itertools import accumulate
input = open(0).readline
input()
L = sorted(list(map(int, input().split())))
L = accumulate(L)
print(sum(L))

