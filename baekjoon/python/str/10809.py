alphabet = [-1] * 26

for idx,i in enumerate(input()):
    if alphabet[ord(i) - ord('a')] == -1:
        alphabet[ord(i) - ord('a')] = idx

for i in alphabet:
    print(i, end=' ')

#### other solution #######################
# string = input()                        #
# alphabet = "abcdefghijklmnopqrstuvwxyz" #
# for i in alphabet:                      #
#     print(string.find(i), end = ' ')    #
###########################################