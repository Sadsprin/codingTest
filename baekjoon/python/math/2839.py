import sys
sugar = int(sys.stdin.readline())
bag = 0 

while True:
    if sugar % 5 == 0:
        bag = bag + sugar // 5
        break
    sugar -= 3
    bag += 1
    if sugar < 0:
        bag = -1
        break


print(bag)
    