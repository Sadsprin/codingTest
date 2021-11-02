a, b = map(int, input().split())


squid = int(b ** 0.5) + 1
prime = [False] * 2 + [True] * (squid - 1)
for i in range(2, squid+1):
    if prime[i] == False: continue
    for j in range(i * i, squid+1, i):
        prime[j] = False
prime_num = []
for idx, i in enumerate(prime):
    if i == True:
        prime_num.append(idx**2)
ans = 0
for i in range(a, b+1):
    for j in range(a, ):
        if i % j == 0:
            ans -= 1
            continue
    ans += 1
print(ans)

