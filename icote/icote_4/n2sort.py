import time
n = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for i in range(len(n)):
#     min_index = i
#     for j in range(i+1, len(n) - 1):
#         if n[i] > n[j]:
#             min_index = j
#     n[i], n[min_index] = n[min_index], n[i]

for i in range(1, len(n)):
    for j in range(i, 0, -1):
        if n[j] < n[j-1]:
            n[j], n[j - 1] = n[j-1], n[j]
        else:
            break
print(n)
