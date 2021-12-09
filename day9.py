#!/usr/bin/env python

import os
import string
import numpy as np
import copy

def check_first(nl,width):
    count = 0
    w = width - 1
    if nl[0][0] < nl[0][1] and nl[0][0] < nl[1][0]:
        count += nl[0][0] + 1

    for i in range(1,w):
        if nl[0][i] < nl[0][i-1] and nl[0][i] < nl[1][i] and nl[0][i] < nl[0][i+1]:
            count += nl[0][i] + 1

    if nl[0][w] < nl[0][w-1] and nl[0][w] < nl[1][w]:
        count += nl[0][w] + 1
    return count


def check_line(nl,width,i):
    count = 0
    w = width - 1
    if nl[i][0] < nl[i][1] and nl[i][0] < nl[i+1][0] and nl[i][0] < nl[i-1][0]:
        count += nl[i][0] + 1

    for j in range(1,w):
        if nl[i][j] < nl[i-1][j] and nl[i][j] < nl[i+1][j] and nl[i][j] < nl[i][j+1] and nl[i][j] < nl[i][j-1] :
            count += nl[i][j] + 1

    if nl[i][w] < nl[i][w-1] and nl[i][w] < nl[i+1][w] and nl[i][w] < nl[i-1][w]:
        count += nl[i][w] + 1
    return count

def check_last(nl,width,height):
    count = 0
    w = width -1
    h = height-1
    if nl[h][0] < nl[h][1] and nl[h][0] < nl[h-1][0]:
        count += nl[h][0] + 1

    for i in range(1,w):
        if nl[h][i] < nl[h][i-1] and nl[h][i] < nl[h-1][i] and nl[h][i] < nl[h][i+1]:
            count += nl[h][i] + 1

    if nl[h][w] < nl[h][w-1] and nl[h][w] < nl[h-1][w]:
        count += nl[h][w] + 1
    return count


count = 0
width = 0
height = 0
tempfile = open("inputDay9.txt")
lines = tempfile.readlines()
num_list = []
for line in lines:
    numbers = line.strip()
    width = len(numbers) if width == 0 else width
    height += 1
    num_list.append(list(map(int,numbers)))

count += check_first(num_list,width)
for i in range(1,height-1):
    count += check_line(num_list,width,i)
count += check_last(num_list,width,height)
print(f"Answer: {count}")
