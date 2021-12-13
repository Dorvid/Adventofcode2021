#!/usr/bin/env python

import os
import string
import numpy as np
import copy
# 1. = 2, 4. = 4, 7. = 3, 8. = 7
# segment_count = [6,2,5,5,4,5,6,3,7,6]

count = 0
tempfile = open("inputDay8.txt")
lines = tempfile.readlines()
for line in lines:
    temp_list = line.split(' | ')
    output = temp_list[1].split(' ')
    output[3] = output[3].strip()

    for i in output:
        length = len(i)
        if length == 2 or length == 4 or length == 3 or length == 7:
            count += 1

print(f"Answer: {count}")