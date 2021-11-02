import sys
from types import resolve_bases
input = sys.stdin.readline
n = int(input())
distance = tuple(map(int, input().split()))
gasstation = tuple(map(int, input().split()))

now_price = int(1e9+1)
result = 0
for i in range(len(gasstation)-1):
    if gasstation[i] < now_price:
        now_price = gasstation[i]
    result += now_price * distance[i]
print(result)



