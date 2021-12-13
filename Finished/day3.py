#!/usr/bin/env python

import os
import string


tempfile = open("inputDay3.txt")
input = tempfile.readlines()
data = list(map(str,input))
data = list(map(lambda s: s.strip(),data))
data_size = len(data)
bit_cnt = [0] * len(data[0])


for i in data:
    for j in range(len(i)):
        if i[j] == '1':
            bit_cnt[j] = bit_cnt[j] + 1

print(bit_cnt)
gamma = ""
epsilon = ""
for i in bit_cnt:
    if i > (data_size - i):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"

answer = int(gamma,base=2) * int(epsilon,base=2)
print("Answer is: " + str(answer))