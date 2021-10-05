from functools import reduce
print(reduce(lambda acc, cur: acc - cur, list(map(eval, input().split("-")))))
