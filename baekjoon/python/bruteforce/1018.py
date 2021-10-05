import sys
input = sys.stdin.readline

n, m = map(int, input().split())
result = []
for i in range(n):
    result.append(list(input().rstrip()))
answer = []
chess88a = ['W', 'B'] * 4
chess88b = ['B', 'W'] * 4
one = [chess88a if i % 2 ==0 else chess88b for i in range(8)]
two = [chess88b if i % 2 ==0 else chess88a for i in range(8)]
min_ = 10 ** 9 - 1
for ii in range(n - 7):
    for jj in range(m - 7):
        for mat in [one, two]:
            ans = 0
            for i in range(8):
                for j in range(8):
                    if result[ii+i][jj+j] != mat[i][j]:
                        ans += 1
            if ans < min_:
                min_ = ans
print(min_)
    




        



