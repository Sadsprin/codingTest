import sys
input = sys.stdin.readline
for _ in range(int(input())):
    zeroFloor = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    K = int(input())
    N = int(input())

    for i in range(K-1):
        for j in range(1,N):
            zeroFloor[j] = zeroFloor[j] + zeroFloor[j-1]
    print(sum(zeroFloor[:N]))