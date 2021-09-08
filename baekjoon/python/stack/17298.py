import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

stack = []
result = []
for i in range(N):
    while stack and A[N - i - 1] >= stack[-1][1]:
        stack.pop()
    if stack: result.append(stack[-1][1])
    else: result.append(-1)
    stack.append((N-i-1,A[N-i-1]))
for i in range(N-1,-1,-1):
    print(result[i], end=' ')