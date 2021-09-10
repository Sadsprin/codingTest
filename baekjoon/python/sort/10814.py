import sys
input = sys.stdin.readline
N = int(input())
res = []
for i in range(N):
    a = input().split()
    a = list(map(lambda x: int(x) if x.isdigit() else x, a))
    res.append(a)

res_sort = sorted(res, key=lambda x :x[0])
for i in res_sort:
    print(i[0],i[1])
