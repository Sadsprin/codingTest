from collections import deque
A = deque(sorted(list(input())))
C = 0
while A[0].isdigit():
    B = A.popleft()
    C += int(B)

print("".join(list(A)) + str(C))