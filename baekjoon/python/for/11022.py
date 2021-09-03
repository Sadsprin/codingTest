import sys
input = sys.stdin

T = int(input.readline())

for idx, result in enumerate(input):
    f, s = map(int, result.split())
    print("Case #{}: {} + {} = {}".format(idx+1, f, s, f+s))