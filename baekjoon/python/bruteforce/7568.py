import sys
input = sys.stdin.readline

N = int(input())
kw = []
for i in range(N):
    a  = list(map(int, input().split()))
    a.append(i)
    kw.append(a)

c = sorted(kw, key = lambda x : -x[0])
print(c)
print(1)
for j in range(N):
    if c[j][1] > c[j + 1][1]:
        print(j+1)
        cur = j+1
    else:
        print(cur)
    
    


      

