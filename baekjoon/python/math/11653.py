# 내 풀이 N이 1이 될때까지 while loop on
# 소인수 분해가 가능한 가장 작은수를 찾는다.
# 그 다음 나눈뒤 다시 가장 작은수를 찾는다.
# 그러나 이 방식의 경우 소인수 분해할 숫자가 다음과 같은
# 경우에도 for루프를 통해 찾아 내야함. 오래걸림
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

while i <= r:
    while not n % i:
        print(i)
        n //= i
    i += 1
if n > 1:
    print(n)