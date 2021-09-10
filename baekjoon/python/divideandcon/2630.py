import sys
input = sys.stdin.readline

def solution(res, x, y, N):
    global one
    global zero
    cur = res[x][y]
    if N == 1:
        if cur == 1: one += 1
        else: zero += 1
        return 
    for i in range(x, x+N):
        for j in range(y, y+N):
            if res[i][j] != cur:
                solution(res, x, y, N//2)
                solution(res, x+N//2, y, N//2)
                solution(res, x, y + N//2, N//2)
                solution(res, x+N//2, y + N//2, N//2)
                return 
    if cur == 1: one +=1
    else: zero += 1


res = []
one = 0
zero = 0
N = int(input())
for i in range(N):
    res.append(list(map(int, input().split())))

solution(res, 0, 0, N)
print(zero)
print(one)
