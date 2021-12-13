#!/usr/bin/env python

import os
import string


tempfile = open("inputDay3.txt")
input = tempfile.readlines()
data = list(map(str,input))
data = list(map(lambda s: s.strip(),data))
bit_cnt = [0] * len(data[0])
o_two = data.copy()
co_two = data.copy()
data_size = len(o_two)
char_to_remove = ''

#Get O^2 rating
for j in range(len(data[0])):
    for i in o_two:
        if i[j] == '1':
            bit_cnt[j] = bit_cnt[j] + 1
    #Select bit to remove from list
    if bit_cnt[j] >= (data_size - bit_cnt[j]):
        char_to_remove = '0'
    else:
        char_to_remove = '1'

    for i in o_two:
        if i[j] == char_to_remove:
            o_two = list(filter(lambda a: a[j]!= char_to_remove,o_two))
    data_size = len(o_two)
print(o_two)
o2_rating = int(o_two[0],base=2)

#Get CO^2 rating
bit_cnt = [0] * len(data[0])
data_size = len(co_two)
for j in range(len(data[0])):
    for i in co_two:
        if i[j] == '1':
            bit_cnt[j] = bit_cnt[j] + 1
    #Select bit to remove from list
    if bit_cnt[j] >= (data_size - bit_cnt[j]):
        char_to_remove = '1'
    else:
        char_to_remove = '0'

    for i in co_two:
        if i[j] == char_to_remove:
            co_two = list(filter(lambda a: a[j]!= char_to_remove,co_two))
    data_size = len(co_two)
    if data_size == 1:
        break
print(co_two)
co2_rating = int(co_two[0],base=2)

print("Answer is: " + str(o2_rating * co2_rating))