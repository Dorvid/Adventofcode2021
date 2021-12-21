#!/usr/bin/env python

import os
import copy


input_file = open("day14input.txt")
first_line = input_file.readline().strip()
print(first_line)


lines = input_file.readlines()

letters = {}
rules = {}
rules_count_base = {}
#Create rules
for line in lines:
    pair,c = line.strip().split(" -> ")
    rules[pair] = (pair[0]+c,c+pair[1],c)
    letters[c] = 0
    rules_count_base[pair] = 0

#Fill letters with letters in first line
for c in first_line:
    letters[c] = letters[c] + 1

rules_count = copy.copy(rules_count_base)
for i in range(len(first_line)-1):
    pair = first_line[i] + first_line[i+1]
    rules_count[pair] = rules_count[pair] + 1

for i in range(40):
    new_rc = copy.copy(rules_count_base)
    for key in rules_count.keys():
        tup = rules[key]
        new_rc[tup[0]] = rules_count[key] + new_rc[tup[0]]
        new_rc[tup[1]] = rules_count[key] + new_rc[tup[1]]
        letters[tup[2]] = letters[tup[2]] + rules_count[key]
    rules_count = new_rc


biggest = 0
smallest = None

for key in letters.keys():
    val = letters[key]
    biggest = val if val > biggest else biggest
    if smallest == None:
        smallest = val
    else:
        smallest = val if val < smallest else smallest
print(biggest-smallest)