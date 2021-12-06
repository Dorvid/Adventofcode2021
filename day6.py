#!/usr/bin/env python

import os
import string
import numpy as np
import copy

class lanternfish:
    counter = 8

    def __init__(self,value:int = 8):
        self.counter = value
    
    def decrement(self):
        self.counter -= 1
        if self.counter == -1:
            return True
        return False
    
    def reset(self):
        self.counter = 6
    


tempfile = open("inputDay6.txt")
first_line = tempfile.readline()
temp_num_list = first_line.split(',')
num_list = list(map(int,temp_num_list))
fish_list = []

for num in num_list:
    fish = lanternfish(num)
    fish_list.append(fish)

for i in range(80):    
    new_fishes = []
    for fish in fish_list:
        if fish.decrement():
            new_fish = lanternfish()
            new_fishes.append(new_fish)
            fish.reset()
    fish_list.extend(new_fishes)

print(f"Answer: {len(fish_list)}")
