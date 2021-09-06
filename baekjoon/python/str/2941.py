croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
croatia_input = input()
sum = 0
for i in croatia:
    sub = croatia_input.count(i)
    if sub == 0: continue
    croatia_input = croatia_input.replace(i, "  ", sub)
    sum += sub
croatia_input = croatia_input.replace("  ", "")
sum += len(croatia_input)
print(sum)