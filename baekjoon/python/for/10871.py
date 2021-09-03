N, X = map(int, input().split())

a = ' '.join([i for i in input().split() if int(i) < X])
print(a)