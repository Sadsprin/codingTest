import sys
input = sys.stdin.readline

for i in range(num := int(input())):
    for j in range(2):
        for k in range(num):
            if j % 2 == 0:
                if k % 2 ==0:
                    print("*",end="")
                else:
                    print(" ",end="")
            else:
                if k % 2 ==0:
                    print(" ",end="")
                else:
                    print("*",end="")                       
        print()


