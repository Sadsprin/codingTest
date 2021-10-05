import sys
input = sys.stdin.readline

N = int(input())
time = []
for i in range(N):
    a, b = map(int, input().split())
    time.append((a, b))
time.sort(key=lambda x: x[1] - x[0], reverse=True)
time.sort(key=lambda x: x[1])
count = 0
end = 0
for i in time:
    if i[0] >= end:
        end = i[1]
        count += 1
print(count)
