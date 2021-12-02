#!/usr/bin/env python

import os
import string


tempfile = open("inputDay2.txt")
input = tempfile.readlines()
h = 0 #horizontal
d = 0 #depth
for line in input:
    data = line.split(" ")
    direction = data[0]
    value = int(data[1].strip())
    if direction == "forward":
        h += value
    elif direction == "up":
        d -= value
    elif direction == "down":
        d += value

print("h:" + str(h) + " d:" + str(d))
print("Answer: " + str(h * d))

    


