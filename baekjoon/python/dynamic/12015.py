from bisect import bisect_left

N = int(input())
arr = list(map(int, input().split()))

answer = [arr[0]]

for i in range(1, N):
    if arr[i] > answer[-1]: answer.append(arr[i])
    else: answer[bisect_left(answer, arr[i])] = arr[i]

print(len(answer))
