num = -1
for i in range(9):
    nn = int(input())
    if nn > num:
        num = nn
        loc = i + 1
print(num)
print(loc)
