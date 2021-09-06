x, y, w, h = map(int, input().split())
if w-x < h-y: print(w - x)
else: print(h - y)