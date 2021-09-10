import sys
input = sys.stdin.readline

def bitonic():
    if N == 1: return 1
    if N == 2: return 2
    max_num = 0
    index = 0
    for i in range(N):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[j] + 1, dp[i])
                if dp[i] > max_num: max_num = dp[i]; index = i
    for i in range(N - 1 - index): dp[index + i + 1] = 1
    for i in range(index+1, N):
        for j in range(index+1, i):
            if arr[i] < arr[j]:
                dp[i] = max(dp[j] + 1, dp[i])
    
    return max_num + max(dp[index+1:])
    
N = int(input())
arr = list(map(int, input().split()))
dp = [1] * N
print(bitonic())

