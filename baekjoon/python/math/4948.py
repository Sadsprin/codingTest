import sys

result_list = []
for i in sys.stdin:
    n = int(i)
    if n == 0: break
    result_list.append(n)

max_n = max(result_list) * 2
num = [True] * (max_n + 1)
max_n_sqrt = int(max_n ** 0.5)

for i in range(2, max_n_sqrt + 1):
    if num[i] == True:
        for j in range(i * i, max_n + 1, i):
            num[j] = False
for i in range(len(result_list)):
    print(num[result_list[i] + 1 : 2 * result_list[i] + 1].count(True))

