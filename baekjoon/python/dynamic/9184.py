import sys
w_cache = [[[0 for i in range(21)] for i in range(21)] for i in range(21)]

def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0: return 1
    if a > 20 or b > 20 or c > 20: return w(20, 20, 20)
    if w_cache[a][b][c] != 0: return w_cache[a][b][c]
    if a < b and b < c: w_cache[a][b][c] =  w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c); return w_cache[a][b][c]
    else:  w_cache[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1); return w_cache[a][b][c]

for i in sys.stdin:
    x,y,z = map(int, i.rstrip().split())
    if x == -1 and y == -1 and z == -1: break
    print("w({}, {}, {}) = {}".format(x,y,z,w(x,y,z)))
    