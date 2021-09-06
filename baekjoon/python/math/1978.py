from functools import partialmethod
import sys
input = sys.stdin.readline

T = int(input())
number = map(int, input().split())
prime = 0
for i in number:
    if i == 1:
        continue
    if i == 2:
        prime += 1
        continue
    for j in range(2, 1001):
        if i > j:
            share, remain = divmod(i, j)
            if share > 1 and remain == 0:
                break
        else:
            prime += 1
            break


print(prime)