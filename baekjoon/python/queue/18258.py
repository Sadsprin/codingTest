from collections import deque
import sys

input = sys.stdin.readline
queue = deque()

def push(value):
    queue.append(value)

def pop():
    return queue.popleft() if not empty() else -1

def size():
    return len(queue)

def front():
    return queue[0] if not empty() else -1

def back():
    return queue[size() - 1] if not empty() else -1

def empty():
    return 1 if size() == 0 else 0

# def printqueue():
#     print('[', end = '')
#     for i in range(size()):
#         print(queue[i], end = ' ')    
#     print(']')



N = int(input())
for _ in range(N):
    ins, *value = input().split()
    if ins == 'push':
        push(int(value[0]))
        # printqueue()
    elif ins == 'pop':
        print(pop())
        # printqueue()
    elif ins == 'size':
        print(size())
        # printqueue()
    elif ins == 'front':
        print(front())
        # printqueue()
    elif ins == 'back':
        print(back())
        # printqueue()
    else:
        print(empty())
        # printqueue()