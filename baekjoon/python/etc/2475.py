import sys
print(sum([int(i) ** 2 for i in sys.stdin.readline().split()]) % 10)