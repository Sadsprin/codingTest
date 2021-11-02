import sys
input = sys.stdin.readline

# 에라토스테네스의 체로 입력 받은 가장 큰수 만큼 소수를 판정하는 리스트를 만든뒤
# 투 포인터를 통해서 front = 2, rear = 소수의 크기 -1 로 설정한 후 front, rear을 코드의 조건문을 이용해 이동한다.
# front와 rear이 엇갈리기 전 최근의 값을 res에 입력한다.
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
    front = i // 2
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


