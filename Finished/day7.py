#!/usr/bin/env python

import os
import string
import numpy as np
import copy

tempfile = open("inputDay7.txt")
first_line = tempfile.readline()
temp_num_list = first_line.split(',')
num_list = list(map(int,temp_num_list))

num_dict = {}
biggest_num = 0
for num in num_list:
    num_dict[num] = num_dict.get(num,0) + 1
    biggest_num = num if num > biggest_num else biggest_num

min_fuel = -1

for i in range(biggest_num):
    fuel = 0
    for key in num_dict:
        fuel += abs(key - i) * num_dict[key]
    
    min_fuel = fuel if min_fuel == -1 or fuel < min_fuel else min_fuel



print(f"Answer: {min_fuel}")
