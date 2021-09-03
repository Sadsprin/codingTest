original= int(input())
newValue = original
ori = original
cycle = 0
while True:
    original = (newValue // 10) + (newValue % 10)
    newValue = int(str(newValue)[-1] + str(original)[-1])
    cycle += 1
    if newValue == ori:
        break
print(cycle)