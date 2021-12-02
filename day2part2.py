#!/usr/bin/env python

import os
import string


tempfile = open("inputDay2.txt")
input = tempfile.readlines()
h = 0 #horizontal
d = 0 #depth
aim = 0
for line in input:
    data = line.split(" ")
    direction = data[0]
    value = int(data[1].strip())
    if direction == "forward":
        #print("Increasing Forward with " + str(data[1]))
        h += value
        d += (value * aim)
    elif direction == "up":
        #print("Increasing Depth with " + str(data[1]))
        aim -= value
    elif direction == "down":
        #print("Decreasing Depth with " + str(data[1]))
        aim += value

print("h:" + str(h) + " d:" + str(d))
print("Answer: " + str(h * d))

    


