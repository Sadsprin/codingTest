import sys
from collections import deque
input = sys.stdin.readline
ans = []
for i in range(int(input())):
    a, b = map(int, input().split())
    dp = [-1] * 10001
    q = deque([(a, "")])
    while q:
        curr, state = q.popleft()
        if dp[int(curr)] != -1: continue
        if curr == b:
            res = state
            break
        dp[int(curr)] = 1
        q.append((curr * 2 % 10000, state+"D"))
        if curr == 0:
            q.append((9999, state + "S"))
        else:
            q.append((curr- 1, state + "S"))
        curr_str = str(curr).zfill(4)   
        q.append((int(curr_str[1:]+curr_str[0]), state + "L"))
        q.append((int(curr_str[-1]+curr_str[0:-1]), state+ "R"))

    ans.append(res)
print(*ans,sep="\n")