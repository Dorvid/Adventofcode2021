#!/usr/bin/env python

import os
import copy


input_file = open("day14input.txt")
first_line = input_file.readline().strip()
print(first_line)

letters = {}
for c in first_line:
    letters[c] = 0

lines = input_file.readlines()

rules = {}
for line in lines:
    pair,insert_val = line.split(" -> ")
    rules[pair] = insert_val.strip()

print(rules)

result = copy.copy(first_line)
for i in range(10): #Inefficient for part 2
    temp = ""
    for j in range(len(result)-1):
        pair = result[j] + result[j+1]
        temp += result[j] + rules[pair]
    temp += result[len(result)-1]
    result = temp
    #print(result)


biggest = 0
smallest = None

for key in letters.keys():
    val = result.count(key)
    letters[key] = val
    biggest = val if val > biggest else biggest
    if smallest == None:
        smallest = val
    else:
        smallest = val if val < smallest else smallest
print(biggest-smallest)