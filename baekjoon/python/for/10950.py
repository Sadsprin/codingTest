import sys
T = int(input())
for result in sys.stdin:
    print(sum(map(int, result.split())))