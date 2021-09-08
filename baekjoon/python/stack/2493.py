import sys
input = sys.stdin.readline

N = int(input())
top = list(map(int, input().split()))

stack = []
result = []
for i in range(len(top)):
        while stack and top[i] >= stack[-1][1]:
            stack.pop()
        if stack: print(stack[-1][0], end=' ')
        else: print(0, end=' ')
        stack.append((i+1, top[i]))
    

        
    


