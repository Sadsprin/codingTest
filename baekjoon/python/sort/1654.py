import sys
input = sys.stdin.readline

def find_lan(N, start, end):
    while True:
        m = (start + end) // 2
        sumoflan = sum(map(lambda x : x // m, lan))
        if start >= end and sumoflan >= N: return m
        if N > sumoflan : end = m - 1
        elif N <= sumoflan: start = m + 1
        



K, N = map(int, input().split())
lan = []
for i in range(K):
    lan.append(int(input()))

print(find_lan(N, 1, max(lan)))


