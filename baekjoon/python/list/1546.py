import sys
from functools import reduce
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))
maxGrade = max(A)
print(maxGrade)
print(reduce(lambda acc, cur : acc + (cur / maxGrade) * 100, A, 0) / N)


