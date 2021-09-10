import sys
N = int(sys.stdin.readline())
stairnum_cache = [[0] * 101 for _ in range(101)]
def stairnum(curr, length):
    if curr > 9 or curr < 0: return 0
    if length == 1: return 1
    if stairnum_cache[curr][length] != 0: return stairnum_cache[curr][length]
    stairnum_cache[curr][length] =  stairnum(curr + 1, length - 1) + stairnum(curr - 1, length -1)
    return stairnum_cache[curr][length]

sum = 0
for i in range(1, 10):
    sum += stairnum(i, N)
print(sum % (10 ** 9))