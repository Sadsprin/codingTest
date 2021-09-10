import sys
input = sys.stdin.readline

T = int(input())
word = set()
for i in range(T): word.add(input().rstrip())


wordSort_1 = sorted(sorted(list(word)), key = lambda x : len(x))
print("\n".join(wordSort_1))

    