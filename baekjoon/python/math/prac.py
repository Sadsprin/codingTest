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
print(prime)

for i in prime:
    if i:
        print(i)