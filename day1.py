#!/usr/bin/env python

import os
import string


tempfile = open("inputDay1.txt")
input = tempfile.readlines()
#data = [[int(val) for val in line.split()]for line in input]
data = list(map(int,input))
cnt = 0

print(data)
for i, j in enumerate(data[:-1]):
    if j < data[i+1]:
        cnt += 1

print("Total increases: " + str(cnt))
