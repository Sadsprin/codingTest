cache = [[1, 0], [0, 1]] + [[0, 0] for i in range(39)]
def fibo(num):
    if cache[num] != [0, 0]: return cache[num]
    fibo1 = fibo(num - 1)
    fibo2 = fibo(num - 2)
    for i in range(2):
        cache[num][i] =fibo1[i] + fibo2[i]
    return cache[num]

T = int(input())
for i in range(T): 
    result = [0, 0]
    a = int(input())
    print(' '.join(list(map(str,fibo(a)))))


