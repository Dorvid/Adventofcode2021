#!/usr/bin/env python

import os
import string
import numpy as np
import copy

count = 0
tempfile = open("inputDay8.txt")
lines = tempfile.readlines()

for line in lines:
    num_dict = {}
    temp_list = line.split(' | ')
    input = temp_list[0].split(' ')
    output = temp_list[1].split(' ')
    output[3] = output[3].strip()

    new_char_pos = ['' for i in range(7)]
    input.sort(key=len)
    # Sorted length =[2,3,4,5,5,5,6,6,6,7] gives us indexs for each number and that indexs 3,4,5 are either 2 3 5 and indexs 6,7,8 are either 0,6,9

    sorted_input = []
    for s in input:
        x = ''.join(sorted(s))
        sorted_input.append(x)
    
    sorted_output = []
    for s in output:
        x = ''.join(sorted(s))
        sorted_output.append(x)

    num_dict[sorted_input[0]] = 1
    chars_in_1 = set(sorted_input[0])
    num_dict[sorted_input[1]] = 7
    #num_dict[sorted_input[3]] = 4
    num_dict[sorted_input[2]] = 4
    num_dict[sorted_input[9]] = 8
    #Find 9 as 4 is a subset of 9
    not_in_9 = None #Set for finding 2 later
    indexs = [6,7,8]
    for i in range(6,9):
        if set(sorted_input[2]).issubset(set(sorted_input[i])):
            num_dict[sorted_input[i]] = 9
            not_in_9 = set("abcdefg") - set(sorted_input[i])
            indexs.remove(i)
            break
    #Find 0 and 6
    #Check if 1 is a subset of 0
    is_six = chars_in_1 - set(sorted_input[indexs[0]]) #Also is the value we need to find that isnt in 5
    if len(is_six) == 1: #We found six
        num_dict[sorted_input[indexs[0]]] = 6
        num_dict[sorted_input[indexs[1]]] = 0
    else:
        is_six = chars_in_1 - set(sorted_input[indexs[1]])
        num_dict[sorted_input[indexs[0]]] = 0
        num_dict[sorted_input[indexs[1]]] = 6
    
    #Find 5
    indexs = [3,4,5]
    for i in range(3,6):
        if not is_six.issubset(set(sorted_input[i])): #Found 5
            indexs.remove(i)
            num_dict[sorted_input[i]] = 5
            break
    
    #If not_in_9 is a subset we have 2 otherwise we have 3
    if not_in_9.issubset(set(sorted_input[indexs[0]])):
        num_dict[sorted_input[indexs[0]]] = 2
        num_dict[sorted_input[indexs[1]]] = 3
    else:
        num_dict[sorted_input[indexs[0]]] = 3
        num_dict[sorted_input[indexs[1]]] = 2
    
    count += num_dict[sorted_output[0]] * 1000 + num_dict[sorted_output[1]] * 100 + num_dict[sorted_output[2]] * 10 + num_dict[sorted_output[3]]

print(f"Answer: {count}")