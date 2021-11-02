import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr_lis = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            arr_lis[i] = max(arr_lis[j] + 1, arr_lis[i])

print(max(arr_lis))