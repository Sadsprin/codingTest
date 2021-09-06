import sys
T = int(sys.stdin.readline())
ans = 1
for i in range(1000000):
    if i == 0:
        T -= 1
    if T - 6 * i > 0:
        T = T - 6 * i
        ans += 1
        continue
    break
print(ans)
    