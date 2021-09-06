import sys
T = int(sys.stdin.readline())
x, y = 1, 1

for i in range(10000000):
    if T - ( ( i**2 + i ) / 2)  <= 0:
        T = int(T - ( ( (i-1) ** 2 + i - 1) / 2))
        can = i - 1
        break
    else:
        continue

if can % 2 != 0:
    y += can
    for i in range(T-1):
        x += 1
        y -= 1
else:
    x += can
    for i in range(T-1):
        x -= 1
        y += 1


print("{}/{}".format(x, y))

    
    