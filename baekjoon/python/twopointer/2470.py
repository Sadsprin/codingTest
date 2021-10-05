import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = len(arr) - 1
ans = 2000000001
while start < end:
    tmp = arr[start] + arr[end]
    if abs(tmp) < abs(ans):
        ans = arr[start] + arr[end]
        ans_list = (arr[start], arr[end])
        if ans == 0: break
    if tmp >= 0: end -= 1
    elif tmp < 0: start += 1
    
print(ans_list[0], ans_list[1])
    
