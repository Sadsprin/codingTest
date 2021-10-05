import sys
input = sys.stdin.readline

def max_tree_size(target, start, end):
    while True:
        mid = (start + end) // 2
        sumoftree = sum(map(lambda x: x - mid if x > mid else 0, arr))
        if start >= end and sumoftree >= target: return mid
        if sumoftree >= target: start = mid + 1
        else: end = mid - 1
    
N, M = map(int, input().split())
arr = list(map(int, input().split()))
print(max_tree_size(M, 0, max(arr)))

