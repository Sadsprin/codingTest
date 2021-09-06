import sys
input = sys.stdin.readline

N, M = map(int, input().split())
card = list(map(int, input().split()))
card.sort(reverse=True)
max = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            cur = card[i] + card[j] + card[k]
            if max < cur and cur <= M:
                max = cur
                break
        
print(max)
