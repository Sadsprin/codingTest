# LIST TREE
# List로 트리를 구현하면 트리가 한쪽으로 치우쳐질 경우 
# 만약 노드가 N개 일 경우 2**N이 되어 메모리 초과가 일어난다.
import sys
input = sys.stdin.readline

n = int(input())
tree = ['.'] * (1<<n)

for i in range(n):
    node, left, right = input().split()
    if tree[1] == '.':
        tree[1] = node
        tree[2] = left
        tree[3] = right
    else:
        k = tree.index(node)
        tree[2*k] = left
        tree[2*k+1] = right

def preorder(start):
    if tree[start] == '.':
        return 
    print(tree[start], end='')
    preorder(start*2)
    preorder(start*2+1)

def inorder(start):
    if tree[start] == '.':
        return 
    inorder(start*2)
    print(tree[start], end='')
    inorder(start*2+1)

def postorder(start):
    if tree[start] == '.':
        return 
    postorder(start*2)
    postorder(start*2+1)
    print(tree[start], end='')
preorder(1)
print()
inorder(1)
print()
postorder(1)

# dict TREE
import sys
input = sys.stdin.readline

n = int(input())
tree = {}

for i in range(n):
    node, left, right = input().split()
    tree[node] = (left, right)

def preorder(start):
    if start == '.':
        return 
    print(start, end='')
    preorder(tree[start][0])
    preorder(tree[start][1])

def inorder(start):
    if start == '.':
        return 
    inorder(tree[start][0])
    print(start, end='')
    inorder(tree[start][1])

def postorder(start):
    if start == '.':
        return 
    postorder(tree[start][0])
    postorder(tree[start][1])
    print(start, end='')
preorder('A')
print()
inorder('A')
print()
postorder('A')

