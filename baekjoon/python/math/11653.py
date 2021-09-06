# N = int(input())
# ForLoop =0
# while N != 1:
#     for i in range(2,10000000):
#         ForLoop += 1
#         if N % i == 0:
#             N = N // i
#             print(i)
#             break
# print(ForLoop)

n = int(input())
i = 2
r = int(n ** 0.5)
ForLoop =0

while i <= r:
    while not n % i:
        ForLoop += 1
        print(i)
        n //= i
    i += 1
if n > 1:
    print(n)
print(ForLoop)