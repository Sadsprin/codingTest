import sys
for i in sys.stdin:
    i = i.rstrip()
    if i == "0": break 
    check = True
    for j in range((length :=len(i)) // 2):
        if i[j] == i[length - j - 1]: continue
        else: check=False; break
    if check: print("yes")
    else: print("no")