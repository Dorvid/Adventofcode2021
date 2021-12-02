#!/usr/bin/env python

import os
import string

tempfile = open("inputDay1.txt")
input = tempfile.read().splitlines()
data = list(map(int,input))
cnt = 0
sum_arr = []
for i, j in enumerate(data[:-2]):
    sum_arr.append(j + data[i+1] + data[i+2])

for i, j in enumerate(sum_arr[:-1]):
    print(j)
    if j < sum_arr[i+1]:
        cnt += 1

print("Total increases: " + str(cnt))
