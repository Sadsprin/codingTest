import sys
S = sys.stdin.readline().rstrip()

operator_rank = {
    '(' : 1,
    '-' : 2,
    '+' : 2,
    '*' : 3,
    '/' : 3  
}

stack = []
ans = ''
for i in S:
    if i.isalpha():
        ans += i
    elif i == '(':
        stack.append(i)
    elif i in '/*':
        while stack and (stack[-1] == "*" or stack[-1] == "/"):
            ans += stack.pop()
        stack.append(i)
    elif i in '+-':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(i)
    elif i == ')':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
    else:
        pass
while stack:
    ans += stack.pop()
print(ans)
