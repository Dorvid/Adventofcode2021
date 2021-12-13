#!/usr/bin/env python

import os
import string
import numpy as np
import copy

tempfile = open("inputDay6.txt")
first_line = tempfile.readline()
temp_num_list = first_line.split(',')
num_list = list(map(int,temp_num_list))
#Solution from github.com/A-UNDERSCORE-D/aoc2021/blob/main/aoc/python/six.py
fish_list = [0 for i in range(9)]

for num in num_list:
    fish_list[num] += 1


for i in range(256):
    new_fishes = [0 for i in range(9)]

    for day, count in enumerate(fish_list):
        if day == 0:
            new_fishes[6] += count
            new_fishes[8] += count
        else:
            new_fishes[day-1] += count
    
    fish_list = new_fishes
#Slow

# for i in range(256):
#     print(i)    
#     new_fishes = []
#     for fish in fish_list:
#         if fish.decrement():
#             new_fish = lanternfish()
#             new_fishes.append(new_fish)
#             fish.reset()
#     fish_list.extend(new_fishes)

print(f"Answer: {sum(fish_list)}")
