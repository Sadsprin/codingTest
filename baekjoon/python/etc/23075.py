import sys
import re
for i in sys.stdin:
    i = i[:-1]
    if i.rstrip() == ".": break
    regex = re.compile("[\]\[\(\)]")
    parenthesis = regex.findall(i)
    stack = []
    check = True
    for j in parenthesis:
        if j == '(' or j == '[': stack.append(j)
        elif j == ')':
            if stack:
                if stack.pop() == "(": continue
                else: check = False
            else: check = False
        else:
            if stack:
                if stack.pop() == '[': continue
                else: check = False
            else: check = False
    if check:
        if stack: print("no")
        else: print("yes")
    else: print("no")


