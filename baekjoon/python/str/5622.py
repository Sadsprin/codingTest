alphabet = list(input())
min_ = 0
for i in alphabet:
    move = (ord(i) - 65) // 3
    if move < 5 : min_ += (move + 3)
    elif i in 'PQRS' : min_ += 8
    elif i in 'TUV' : min_ += 9
    elif i in 'WXYZ' : min_ += 10
    else: min_ += 10
print(min_)
