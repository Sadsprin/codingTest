import sys
input = sys.stdin.readline

def quadTree(x, y, N):
    global res
    cur = res[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if cur != res[i][j]:
                return "(" + str(quadTree(x, y, N//2)) + str(quadTree(x , y + N//2, N//2)) + str(quadTree(x + N//2, y, N//2)) + str(quadTree(x + N//2, y + N//2, N//2)) + ")"
    if cur == 1: return 1
    else: return 0
    

res = []
N = int(input())
for i in range(N):
    res.append(list(map(int, list(input().rstrip()))))
print(quadTree(0,0,N))

