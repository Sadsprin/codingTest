from sys import stdin, stdout

def bisect_cus(target, start, end):

    while True:
        mid = (start + end) // 2
        if arr[mid] == target: return '1'
        elif start >= end: return '0'
        elif target < arr[mid] : end = mid - 1
        else: start = mid + 1

N = int(stdin.readline())
arr = sorted(list(map(int, stdin.readline().split())))
start = 0
end = N - 1
M = int(stdin.readline())
M_arr = map(int, stdin.readline().split())
for i in M_arr: stdout.write(bisect_cus(i, start, end) + '\n')


