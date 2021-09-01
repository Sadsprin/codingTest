import sys

def segtree_init(node, start, end):
    if start == end:
        tree[node] = data[start]
    else:
        f = segtree_init(node*2, start, (start + end) //2)
        s = segtree_init(node*2+1, (start + end)// 2 + 1, end)
        tree[node] = f if f < s else s
    return tree[node]

def range_min_value(node, start, end, left, right):
        if start > right or end < left:
            return float('inf')
        elif left <= start and end <= right:
            return tree[node]
        else:
            mid = (start + end) // 2
        return min(range_min_value(node * 2, start, mid, left, right), range_min_value(node * 2 + 1, mid + 1, end, left, right))

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    data = [int(sys.stdin.readline().rstrip()) for i in range(N)]
    tree = [0] * N * 4
    result = []
    segtree_init(1, 0, N - 1)
    for j in range(M):
        left, right = map(int, sys.stdin.readline().split())
        result.append(range_min_value(1, 0, N -1, left-1, right-1))

    for i in result:
        print(i)
