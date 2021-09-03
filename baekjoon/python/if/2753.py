# Author : sadspring
# Date : 2021 / 09 / 02
# reference : No

year = int(input())

def isleafYear(year):
    if year % 400 == 0:
        return 1
    elif year % 4 == 0 and year % 100 != 0:
        return 1
    return 0

print(isleafYear(year))

