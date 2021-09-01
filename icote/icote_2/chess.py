import sys 
N = list(sys.stdin.readline().rstrip())
x = int(N[1]) - 1
y = int(ord(N[0])) - int(ord('a'))
pan = [[0] * 8 for _ in range(8)]
move = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
possible = 0

for move_ in move:
    nx = x + move_[0]
    ny = y + move_[1]
    if nx < 0 or ny < 0 or nx > 7 or nx > 7:
        continue
    possible += 1
print(possible)

