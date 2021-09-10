import sys
input = sys.stdin.readline

def solution(x, y, N):
    global res
    global one
    global zero
    global minusone
    cur = res[x][y]
    for i in range(x, x+N):
        for j in range(y, y+N):
            if res[i][j] != cur:
                solution(x, y, N//3)
                solution(x, y + N//3, N//3)
                solution(x, y + N//3 * 2, N//3)
                solution(x + N//3, y, N//3)
                solution(x + N//3, y + N//3, N//3)
                solution(x + N//3, y + N//3 * 2, N//3)
                solution(x + N//3 * 2, y, N//3)
                solution(x + N//3 * 2, y + N//3, N//3)
                solution(x + N//3 * 2, y + N//3 * 2, N//3)
                return 
    if cur == 1: one +=1
    elif cur == -1: minusone += 1
    else: zero += 1


res = []
one = 0; zero = 0; minusone = 0
N = int(input())
for i in range(N):
    res.append(list(map(int, input().split())))
solution(0,0,N)
print(minusone)
print(zero)
print(one)