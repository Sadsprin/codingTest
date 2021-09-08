import sys
input = sys.stdin.readline

T = int(input())
num_list = []
for _ in range(T):
    num_list.append(int(input()))

max_value = max(num_list)

max_sqrt = int(max_value ** 0.5)

prime = [False] * 2 + [True] * (max_value - 1)

for i in range(2, max_sqrt):
    if prime[i] == True:
        for j in range(i * i, max_value, i):
            prime[j] = False
for i in num_list:
    front = 2
    rear = i - 1
    res_left, res_right = 0,0
    while front <= rear:
        while prime[front] == False:
            if front > i - 1:
                break
            front += 1

        while prime[rear] == False:
            if rear < 2:
                break
            rear -= 1

        if front + rear == i:
            res_left, res_right = front, rear
            front += 1
            rear += 1
        elif front + rear > i:
            rear -= 1
        else:
            front += 1
    print(res_left, res_right)


