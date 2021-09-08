import sys

input = sys.stdin.readline

n = int(input())
num = sorted(list(map(int, input().split())))
x = int(input())



front = 0
rear = len(num) - 1
res = 0
while front < rear:
    if num[front] + num[rear] == x:
        res += 1
        front += 1
    elif num[front] + num[rear] > x:
        rear -= 1
    else:
        front += 1
print(res)

    

    

