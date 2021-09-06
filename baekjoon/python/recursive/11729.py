## failure ##
def hanoi(n, start, end, middle):
    if n == 1:
        print(start, "->", end)
        return
    hanoi(n - 1, start, middle, end)
    print(start, "->", end)
    hanoi(n - 1, middle, end, start)

hanoi(2,1,3,2)
