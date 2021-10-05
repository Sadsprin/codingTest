import sys
from pprint import pprint
read = sys.stdin.readline
num = int(read())
graph = [[] for i in range(num)]
for i in range(num):
    for j in range(num):
        if i == 0 or i == num - 1 or j == 0 or j == num - 1 or i == j or i + j == num - 1:
            graph[i].append("*")
        else:
            graph[i].append(" ")

for i in range(num):
    print("".join(graph[i]))



