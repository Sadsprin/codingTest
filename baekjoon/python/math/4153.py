import sys

for i in sys.stdin:
    a,b,c =  map(int,i.split())
    if a+b+c == 0:
        break
    
    max_value = max(a,b,c)

    if max_value == a:
        if b ** 2 + c ** 2 == a ** 2:
            print("right")
        else:
            print("wrong")
    elif max_value == b:
        if a ** 2 + c ** 2 == b ** 2:
            print("right")
        else:
            print("wrong")
    else:
        if a ** 2 + b ** 2 == c ** 2:
            print("right")
        else:
            print("wrong")