import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
N, r, c = map(int, input().split())
def divandcon(N, x, y, num):
    global res
    if N == 0 and x == r and y == c:
        res = num
        return
    if x <= r < x + 2 ** (N - 1) and y <= c < y + 2 ** (N - 1):
        divandcon(N - 1, x, y, num)
    elif x <= r < x + 2 ** (N - 1) and y + 2 ** (N - 1) <= c < y + 2 ** (N):
        divandcon(N - 1, x, y + 2 ** (N - 1), num + 4 ** (N - 1))
    elif x + 2 ** (N - 1) <= r < x + 2 ** (N) and y <= c < y + 2 ** (N - 1):
        divandcon(N - 1, x + 2 ** (N - 1), y, num + 2 * 4 ** (N - 1))
    elif x + 2 ** (N - 1) <= r < x + 2 ** (N) and y + 2 ** (N - 1) <= c < y + 2 ** (N):
        divandcon(N - 1, x + 2 ** (N - 1), y + 2 ** (N - 1), num + 3 * 4 ** (N - 1))

res = 0
divandcon(N, 0, 0, 0)
print(res)