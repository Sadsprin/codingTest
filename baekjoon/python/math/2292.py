import sys
T = int(sys.stdin.readline())
ans = 1
for i in range(1000000):
    if T - 6 * i > 0:
        T = T - 6 * i if i != 0 else T - 1
        ans += 1
        continue
    break
print(ans)
    