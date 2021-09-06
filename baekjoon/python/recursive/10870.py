# N = int(input())
# fiboList = [0] * (N+1)
# def fibo(num):
#     if num == 0: return 0
#     if num == 1: return 1
#     if fiboList[num] != 0: return fiboList[num]
#     fiboList[num] = fibo(num - 1) + fibo(num - 2)
#     return fiboList[num]

# print(fibo(N))

def p(n):
    x=0;y=1
    for i in range(n):
        x,y = y, x+y
    return x

a = int(input())
print(p(a))