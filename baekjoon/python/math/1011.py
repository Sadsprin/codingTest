import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    start, end = map(int, input().split())
    distance = end - start
    distance_2 = distance ** (1/2)
    if int(distance_2) == distance_2:
        move = int(distance_2) * 2 - 1
    elif distance > int(distance_2) ** 2 + distance_2:
        move = int(distance_2) * 2 + 1
    else:
        move = int(distance_2) * 2
    print(move)
    

            

        
