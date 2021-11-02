import sys
from collections import deque
input = sys.stdin.readline
write = sys.stdout.write
def sol():
    for i in range(int(input())):
        f = input().rstrip()
        f = f.replace("RR", "", len(f))
        n = int(input())
        try:
            L = deque([*map(int, input()[1:-2].split(","))])
        except ValueError:
            L = []
        check = False
        r_check = False
        for i in f:
            if i == "R" : r_check ^= True
            elif i == "D":
                if L:
                    if r_check: L.pop()
                    else: L.popleft()
                else:
                    check = True
                    write("error\n")
                    break
        if r_check: L.reverse()
        if not check: write("["+",".join(map(str,L))+"]"+"\n")
sol()
