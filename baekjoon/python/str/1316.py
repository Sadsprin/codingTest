
def judge(data):
    prev = ''
    stack = []
    for i in data:
        if prev == i:
            prev = i
            continue
        prev = i
        if i not in stack:
            stack.append(i)
        else:
            return False
    return True

T = int(input())
sum=0
for _ in range(T):
    sum += (1 if judge(input()) else 0)
print(sum)

a = 'helloh'
sorted(a, key=a.find)