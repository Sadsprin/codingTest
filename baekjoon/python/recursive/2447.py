import sys
def subStar(max,num, ix, jy, div3):
    for i in range(ix + div3 ,ix + num - div3):
        for j in range(jy + div3 ,jy + num  - div3):
            if i >= max or j >= max: continue
            fullstar[i][j] = ' '


def subSquare(max, num):
    div3 = int(num / 3)
    for i in range(0, max, num):
        for j in range(0, max, num):
            subStar(max, num, i, j, div3)
    if num == 3: return
    else: return subSquare(max, div3)

N = int(sys.stdin.readline())
fullstar = [['*'] * N for _ in range(N)]
subSquare(N, N)

for i in fullstar:
    for j in i:
        print(j, end='')
    print()