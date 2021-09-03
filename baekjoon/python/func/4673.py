


a = list(range(10001))
b = list(range(10001))
for i in a:
    if i == 0 : continue
    while True:
        next = i + sum(map(int,list(str(i))))
        if next > 10000: break
        if b[next] == 0: break
        b[next] = 0
for i in b:
    if i != 0:
        print(i)