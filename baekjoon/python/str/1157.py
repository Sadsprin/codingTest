
alpha = input().lower()
set_alpha = set(alpha)
complex = False
cur = 0
for i in set_alpha:
    count_alpha = alpha.count(i)
    if count_alpha == cur:
        complex = True
        continue
    if count_alpha > cur:
        cur = count_alpha
        cur_alpha = i
        complex = False

if not complex:
    print(cur_alpha.upper())
else:
    print('?')

