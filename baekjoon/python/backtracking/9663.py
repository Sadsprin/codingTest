# N-Queen 
# Queen : 가로, 세로, 대각선으로 움직일 수 있는 체스 말
# 0 다른 퀸이 공격할 수 없는 공간 1 다른 퀸이 공격할 수 있는 공간
# 5 x 5
#     Q 1 1 1 1
#     1 1 0 0 0
#     1 0 1 0 0
#     1 0 0 1 0
#     1 0 0 0 1
def check(index, rows):
    global row
    if rows == 1:
        return False
    for i in range(1, rows+1):
        if row[i] == index or (abs(i - rows) == abs(row[i] - index)):
            return True
    return False

def dfs(rows):
    global ans
    if rows > n:
        ans += 1
        return

    for i in range(1, n + 1):
        if i in row: continue
        if check(i, rows): continue
        else:
            row[rows] = i
            dfs(rows + 1)
            row[rows] = n + 1        

ans = 0
n = int(input())
row = [n+1] * (n + 1)
columns = [n+1] * (n + 1)
dfs(1)
print(ans)