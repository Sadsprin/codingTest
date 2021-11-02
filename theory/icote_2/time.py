import sys
N = int(sys.stdin.readline())
import time
start = time.time()
m = 0
num = 0
while m < 60:
    if '3' in str(m):
        print(m)
        num += 60
    else:
        num += 15
    m += 1
print(num)
num_3 = 3600
result = 0
h = 0
while h <= N:
    if h in [3, 13, 23]:
        result += num_3
    else:
        result += num
    h +=1

    

print(result)