import sys
from math import pi
radius = int(sys.stdin.readline())
print(round(radius ** 2 * pi,6))
print("%.6f" % ((radius * 2) ** 2 / 2))