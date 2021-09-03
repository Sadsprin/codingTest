import sys
input = sys.stdin

T = int(input.readline())

for result in input:
    sys.stdout.write(sum(map(int, result.split())))

