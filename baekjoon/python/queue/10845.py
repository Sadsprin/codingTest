from collections import deque
from sys import stdin
class queue:
    def __init__(self):
        self.queue = deque()
        self.length = 0
    
    def push(self, num):
        self.length += 1
        self.queue.append(num)
    
    def pop(self):
        if self.isEmpty():
            return -1
        else:
            self.length -= 1
            return self.queue.popleft()

    def size(self):
        return self.length
    
    def front(self):
        return -1 if self.isEmpty() else self.queue[0]
    
    def back(self):
        return -1 if self.isEmpty() else self.queue[-1]
    
    def isEmpty(self):
        return True if self.size() == 0 else False


n = int(stdin.readline())
Queue = queue()
for i in stdin:
    i = i.split()
    if i[0] == 'push':
        Queue.push(i[1])
    elif i[0] == 'front':
        print(Queue.front())
    elif i[0] == 'back':
        print(Queue.back())
    elif i[0] == 'size':
        print(Queue.size())
    elif i[0] == 'empty':
        print('1' if Queue.isEmpty() else '0')
    else:
        print(Queue.pop())
    
