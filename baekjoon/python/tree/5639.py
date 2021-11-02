import sys
sys.setrecursionlimit(10**9)
from bisect import bisect_left
MAX = int(1e9)
class Node:
    def __init__(self, data, left, right):
        self.value = data
        self.left = left
        self.right = right

def sol(s, e):
    if not (0 <= s < len(L) and 0 <= e < len(L)):
        return None
    if s == e:
        return Node(L[s], None, None)
    root = L[s]
    mid = bisect_left(L, root, lo=s+1, hi=e+1)
    left = None
    right = None
    if mid > s + 1:
        left = sol(s+1, mid-1)
    if mid <= e:
        right = sol(mid, e)
    return Node(root, left, right)
    
def post(root):
    if root == None:
        return 
    post(root.left)
    post(root.right)
    print(root.value)

L = []
for i in sys.stdin:
    if i == "\n": break
    L.append(int(i))
tree = sol(0, len(L)-1)
post(tree)



