N = int(input())
res = 0
while N != 1:
    if N % 5 == 0:
        N //= 5
    elif N % 3 == 0:
        N //= 3
    elif N % 2 == 0:
        N //= 2
    else:
        N -= 1
    print(N)
    res += 1
print(res)